import random
import paho.mqtt.client as mqtt
import json  
import datetime 
import time

# Time format
TimeFormat = '%m/%d %H:%M:%S'

# Inital the Client object
client = mqtt.Client()

# Setting the MQTT's IP, Port and keepalive time
client.connect("10.0.0.51", 1883, 60)

while True:
    Temperture = random.randint(5,55) #Here is the random data 
    t = datetime.datetime.now().strftime(TimeFormat) #Making the timestamp data
    payload = {'Temperature' : Temperture , 'Time' : t} #Here is making the payload or MQTT by Json format.
    print (json.dumps(payload))# Transfer payload to MQTT
    client.publish("/TestMQTT", json.dumps(payload)) #Publish the MQTT
    time.sleep(1)
