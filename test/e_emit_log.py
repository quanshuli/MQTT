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

routing_key = 'test1'
message = 'Hello World!'

channel.basic_publish(
    exchange=exchangeName, routing_key=routing_key, body=message)

print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()