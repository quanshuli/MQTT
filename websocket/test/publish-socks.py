'''
web socket test
'''
import paho.mqtt.client as paho
import time
#broker="broker.mqttdashboard.com"
#broker="iot.eclipse.org"
#broker="localhost"
broker="192.168.0.11"
port= 9001
#broker="127.0.0.1"
#port=1883
#port= 80


sub_topic="test"

client= paho.Client("publish-socks",transport='websockets')       #create client object
#client= paho.Client("publish-socks") # no websocket

client.connect(broker,port)           #establish connection

while True:
   client.publish(sub_topic,"test message")    #publish
   print('publishing: test message')
   time.sleep(1)




