'''
mqtt through rabbitmq
'''
import pika, sys, json, time

mqttBrokerHost = '127.0.0.1'
mqttBrokerPort = 1883
mqttUser = 'guest'
mqttPassword = 'guest'
mqttTopic = 'generated_numbers'
mqttClientId = 'Numbers'

# set up the credentials same as mqtt publisher
user_pwd = pika.PlainCredentials(mqttUser, mqttPassword)



# set up connections in rabbitmq
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=mqttBrokerHost, 
        #credentials=user_pwd
    ))
channel = connection.channel()

# define exchange info
exchangeTopic = 'amq.topic'
exchangeType = 'topic'

# declare exchange info
channel.exchange_declare(
    exchange=exchangeTopic, exchange_type=exchangeType, durable=True
)

# declare queue, delete the queue when consumer quits
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# binding keys
binding_key = mqttTopic

# binding queues
channel.queue_bind(
    exchange=exchangeTopic, queue=queue_name, routing_key=binding_key)

# set up callback
def callback(ch, method, properties, body):
    print(' [x] Received %r' % body.decode())
    #ch.basic_ack(delivery_tag=method.delivery_tag)

#channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      # auto_ack: redeliver if not consumed
                      # auto_ack=True, # no message acknowledgment with True
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()