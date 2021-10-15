'''
web socket test
'''
import paho.mqtt.client as mqtt
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

 
def on_message(client, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))


client= mqtt.Client("receive-socks",transport='websockets')       #create client object
#client= mqtt.Client("receive-socks") # no websocket

client.connect(broker,port)           #establish connection

client.loop_start()

client.subscribe(sub_topic)
client.on_message = on_message        #assign function to callback

time.sleep(30)
client.loop_stop()



