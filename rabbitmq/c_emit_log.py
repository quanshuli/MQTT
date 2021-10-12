'''
use exchange_declare
'''
import pika, sys
#from pika import exchange_type

# broker: localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# exchange types: direct, topic, headers and fanout
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message
                      )
print(' [x] Sent %r ' % message)

connection.close()