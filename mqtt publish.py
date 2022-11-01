#Task 1 Writing a random number generator publishing a random number between 1 and 100 to MOSQUITTO MQTT Broker
#Interval is random between 1 and 30 seconds
#Broker Topic name is set as "Random-number"
# using Paho MQTT as client

import paho.mqtt.client as mqtttest
import random
import time

# connection to the broker
mqttbroker = "test.mosquitto.org"
client = mqtttest.Client("Random-number")
client.connect(mqttbroker)

while True:
    randrange = random.randint(1, 100)
    randomTime = random.randint(1, 30)
    client.publish("Random-number", randrange)
    print("publish " + str(randrange) + " to MOSQUITTO MQTT Topic")
    time.sleep(randomTime)
