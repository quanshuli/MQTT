'''
exchange_type='topic'
'''
import pika, sys


connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='amq.topic', exchange_type='topic', durable=True)

result = channel.queue_declare('', exclusive=True, durable=True)
queue_name = result.method.queue

binding_key = 'amq.topic'

channel.queue_bind(
    exchange='amq.topic', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()                         