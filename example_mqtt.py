import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

# Time format
ISOTIMEFORMAT = '%m/%d %H:%M:%S'

# Inital the Client object
client = mqtt.Client()

# Setting the MQTT's IP, Port and keepalive time
client.connect("10.0.0.51", 1883, 60)

while True:
    Temperture = random.randint(0,30)
    t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    payload = {'Temperature' : Temperture , 'Time' : t}
    print (json.dumps(payload))
    #THis
    client.publish("/TestMQTT", json.dumps(payload))
    time.sleep(1)
