#In this task, a third python application is subscribing to topic "AVERAGES/1"
#And prints the averages in a tabular format


import paho.mqtt.client as mqtttest
from prettytable import PrettyTable

table_averages = PrettyTable()
table_averages.field_names = ["Average One", "Average Five", "Average Thirty"]


def message(client, userdata, message):

    average_one = 0
    average_five = 0
    average_thirty = 0

    message_received = str(message.payload.decode("utf-8"))

    topic_received = message.topic

    if topic_received == "Averages/1":
        average_one = float(message_received)
    elif topic_received == "Averages/5":
        average_five = float(message_received)
    elif topic_received == "Averages/30":
        average_thirty = float(message_received)

    table_averages.add_row([average_one, average_five, average_thirty])
    print(table_averages)


mqttbroker = "test.mosquitto.org"
client = mqtttest.Client("STATISTICS")
client.connect(mqttbroker)

client.subscribe("Averages/1")
client.subscribe("Averages/5")
client.subscribe("Averages/30")
client.on_message = message


while True:
    client.loop()
