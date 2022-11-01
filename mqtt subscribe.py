#In this task, a python application has subscribed to the topic "Random-number" 
#The application is calculating averages of the data published by broker at 1 minute, 5 minute and 30 minutes
#After calculating averages, the application is publishing these averages to a different topic "AVERAGES/1"

import paho.mqtt.client as mqtttest
import schedule

list_one = []
list_two = []
list_three = []


def message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("Received " + message)
    list_one.append(float(message))
    list_two.append(float(message))
    list_three.append(float(message))


# connection to the broker
mqttbroker = "test.mosquitto.org"
client = mqtttest.Client("Averages")
client.connect(mqttbroker)

client.subscribe("Random-number")
client.on_message = message

# Client calculating the 1 minute,5 minutes and 30 minutes averages


def average(list):
    if len(list) == 0:
        average = 0
    else:
        average = sum(list)/len(list)
    return average


def one_minute_average():
    average_one = average(list_one)
    print('AVERAGE after 1 minute is', average_one)
    client.publish("Averages/1", average_one)
    list_one.clear()
    print("publish" + str(average_one) + " to MOSQUITTO avg topic")


schedule.every(10).seconds.do(one_minute_average)


def five_minute_average():
    average_five = average(list_two)
    print('AVERAGE after 5 minutes is', average_five)
    client.publish("Averages/5", average_five)
    list_two.clear()
    print("publish " + str(average_five) + " to MOSQUITTO avg topic")


schedule.every(5).minutes.do(five_minute_average)


def thirty_minute_average():
    average_thirty = average(list_three)
    print('AVERAGE after 30 minutes is', average_thirty)
    client.publish("Averages/30", average_thirty)
    list_three.clear()
    print("publish " + str(average_thirty) + " to MOSQUITTO  avg topic")


schedule.every(30).minutes.do(thirty_minute_average)

while True:
    client.loop()
    schedule.run_pending()
