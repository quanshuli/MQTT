'''
   - using paho.mqtt to send numbers through mosquitt.
   - using websocket setting.
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

# define the topic 
sub_topic="test"

#create client object
client= mqtt.Client("publish-socks",transport='websockets')       
#client= paho.Client("publish-socks") # no websocket

#establish connection
client.connect(broker,port)           

# continuously sending signals 
while True:
   # generate the random integer for sending
   rand_int = random.randint(1, 100)
   
   # get the time when sending
   now = datetime.utcnow().microsecond # utc time with microsecond only
   #now = datetime.now(timezone.utc).isoformat() # aware time object
   #now = datetime.utcnow().isoformat() # utc time

   # serializing the message into json format
   msg = json.dumps({'UTC_TIME_MICROSEC': now,
                     'NUMBER': rand_int})

   # send out the message
   client.publish(sub_topic,msg)    

   print('publishing: ', msg)

   # set intervals
   time.sleep(1)


