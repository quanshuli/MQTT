'''
local host working with mosquitto
'''
import paho.mqtt.client as mqtt
import time
import json

port=1883 # working with conf setting portal: mqtt
#port=9001
def on_message(client, userdata, message):
    m_decode = str(message.payload.decode('utf-8'))
    m_json = json.loads(m_decode)
    print(m_json)

mqttBroker = 'localhost'
#mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('receiver')
client.connect(mqttBroker, port)

client.loop_start()

client.subscribe('test1')

client.on_message=on_message

time.sleep(30)
client.loop_stop()
