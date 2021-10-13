'''
mqtt through rabbitmq
'''
import pika, sys, json, time

from pika import exchange_type
from mqtt_publish import mqttPassword, mqttUser, mqttBrokerHost, \
                          mqttTopic

# set up the credentials same as mqtt publisher
user_pwd = pika.PlainCredentials(mqttUser, mqttPassword)

# define exchange info
exchangeTopic = 'amq.topic'
exchangeType = 'topic'

# set up connections in rabbitmq
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        mqttBrokerHost, credentials=user_pwd
    ))
channel = connection.channel()

# declare exchange info
channel.exchange_declare(
    exchange=exchangeTopic, exchange_type=exchangeType, durable=True
)

# declare queue, delete the queue when consumer quits
result = channel.queue_declare(exclusive=True)

# random queue name
queue_name = result.method.queue

# binding keys
binding_keys = [mqttTopic]

# binding queues
channel.queue_bind(
    exchange=exchangeTopic, queue=queue_name, routing_key=binding_keys)

# set up callback
def callback(ch, method, properties, body):
    print(' [x] Received %r' % body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      # auto_ack: redeliver if not consumed
                      # auto_ack=True, # no message acknowledgment with True
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()