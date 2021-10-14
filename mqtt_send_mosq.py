'''
local host working with mosquitto
'''
#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
import json 

port=1883 # working
#port=9001 # not working with mosquitto conf portal websocket
mqttBroker = 'localhost'
#mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('publisher')
client.connect(mqttBroker, port)

while True:
    rand_int = random.randint(1, 100)
    now = datetime.now().isoformat()

    MQTT_MSG = json.dumps({'TIME_STAMP': now,
                           'NUMBER': rand_int})

    client.publish('test1', MQTT_MSG)

    print(MQTT_MSG)

    time.sleep(1)