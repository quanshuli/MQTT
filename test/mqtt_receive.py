'''
local host working with mosquitto
'''
import paho.mqtt.client as mqtt
import time
import json

def on_message(client, userdata, message):
    m_decode = str(message.payload.decode('utf-8'))
    m_json = json.loads(m_decode)
    print(m_json)

mqttBroker = 'localhost'
#mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('receiver')
client.connect(mqttBroker, 1883)

client.loop_start()

client.subscribe('amq.topic')

client.on_message=on_message

time.sleep(30)
client.loop_stop()
