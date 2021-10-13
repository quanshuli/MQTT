'''
mqtt through rabbitmq
'''
#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import random, time, json
from datetime import datetime
 
mqttBrokerHost = '127.0.0.1'
mqttBrokerPort = 1883
mqttUser = 'guest'
mqttPassword = 'guest'
mqttTopic = 'generated_numbers'
mqttClientId = 'Numbers'

mqtt_client = mqtt.Client(mqttClientId)
mqtt_client.connect(mqttBrokerHost, mqttBrokerPort)

while True:
    rand_int = random.randint(1, 100)
    now = datetime.now().isoformat()
    MQTT_MSG = json.dumps({'TIME_STAMP': now,
                           'NUMBER': rand_int})
    mqtt_client.publish(mqttTopic, MQTT_MSG)
    print(MQTT_MSG)
    time.sleep(1)


    


#print(rand_int)
#publish.single('paho/test/single', hostname="localhost", port=1883)
#client.publish('RANDOM_NUMBER', rand_int)
#print('Published ' + str(rand_int) + ', topic RANDOM_NUMBER')
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




