"""   
   - Using paho.mqtt to send numbers through mosquitto.
   - Using websocket setting.
"""

import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime, timezone
import json 

# Websocket setting:
broker = "192.168.0.11"
port = 9001

# Mqtt setting:
#broker="127.0.0.1"
#port=1883
#port= 80

# Define the topic 
sub_topic = "test"

# Create client object
client = mqtt.Client("publish-socks", transport='websockets')       
#client= paho.Client("publish-socks") # no websocket

# Establish connection
client.connect(broker, port)           

# Continuously sending signals 
while True:
   # Generate the random integer for sending
   rand_int = random.randint(1, 100)
   
   # Get the time when sending
   # Utc time with microsecond only
   now = datetime.utcnow().microsecond 
   
   #now = datetime.now(timezone.utc).isoformat() # aware time object
   #now = datetime.utcnow().isoformat() # utc time

   # Serializing the message into json format
   msg = json.dumps({'UTC_TIME_MICROSEC': now,
                     'NUMBER': rand_int})

   # Send out the message
   client.publish(sub_topic, msg)    

   print('publishing: ', msg)

   # Set intervals
   time.sleep(1)


