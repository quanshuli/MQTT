'''
broker: 'mqtt.eclipseprojects.io'
'''
import paho.mqtt.client as mqtt
import time
import json

def on_message(client, userdata, message):
    m_decode = str(message.payload.decode('utf-8'))
    m_json = json.loads(m_decode)
    print(m_json)

mqttBroker = 'mqtt.eclipseprojects.io'

client = mqtt.Client('WebApp')
client.connect(mqttBroker)

client.loop_start()

client.subscribe('RANDOM_NUMBER')

client.on_message=on_message

time.sleep(30)
client.loop_stop()

'''import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = 'localhost'
port_number = 1883'''