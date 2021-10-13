'''
exchange_type='topic'
'''
import pika, sys

connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchangeName = 'matt-rabit'
exchangeType = 'topic'

channel.exchange_declare(exchange=exchangeName, exchange_type=exchangeType)

result = channel.queue_declare('quene-test')

binding_key = 'test1'

channel.queue_bind(
    exchange=exchangeName, queue='quene-test', routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(
    queue='quene-test', on_message_callback=callback, auto_ack=True)

channel.start_consuming()