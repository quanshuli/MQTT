'''
local host working with mosquitto
'''
#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
import json 
 
mqttBroker = 'localhost'
#mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('publisher')
client.connect(mqttBroker, 1883)

while True:
    rand_int = random.randint(1, 100)
    now = datetime.now().isoformat()

    MQTT_MSG = json.dumps({'TIME_STAMP': now,
                           'NUMBER': rand_int})

    client.publish('amq.topic', MQTT_MSG)

    print(MQTT_MSG)

    time.sleep(1)