'''
   using web socket to send numbers
'''
import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime, timezone
import json 

# websocket setting:
broker="192.168.0.11"
port= 9001

# mqtt setting:
#broker="127.0.0.1"
#port=1883
#port= 80

sub_topic="test"

client= mqtt.Client("publish-socks",transport='websockets')       #create client object
#client= paho.Client("publish-socks") # no websocket

client.connect(broker,port)           #establish connection

while True:
   rand_int = random.randint(1, 100)
   #now = datetime.utcnow().isoformat() # utc time
   now = datetime.utcnow().microsecond # utc time with microsecond only
   #now = datetime.now(timezone.utc).isoformat() # aware time object

   msg = json.dumps({'UTC_TIME_MICROSEC': now,
                     'NUMBER': rand_int})
   client.publish(sub_topic,msg)    #publish
   print('publishing: ', msg)
   time.sleep(1)


