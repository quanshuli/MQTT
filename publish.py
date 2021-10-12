'''
broker: 'mqtt.eclipseprojects.io'
'''
#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
# try to use json for timestamp info 
# but datetime.datetime is not json serializable 
import json 
 
mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('Numbers')
client.connect(mqttBroker)

while True:
    rand_int = random.randint(1, 100)
    now = datetime.now().isoformat()
    MQTT_MSG = json.dumps({'TIME_STAMP': now,
                           'NUMBER': rand_int})
  
    #print(rand_int)
    #publish.single('paho/test/single', hostname="localhost", port=1883)
    client.publish('RANDOM_NUMBER', MQTT_MSG)
    #client.publish('RANDOM_NUMBER', rand_int)
    #print('Published ' + str(rand_int) + ', topic RANDOM_NUMBER')
    print(MQTT_MSG)
    time.sleep(1)



'''
import rabbitpy
creates a queue named mqtt-messages,  
binds it to the amq.topic, 
exchange using the routing key #.

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'mqtt-messages')
        queue.declare()
        queue.bind('amq.topic', '#')
'''




