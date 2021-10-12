import pika

# broker: localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# send the message to quene: hello
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(' [x] Sent "Hello World!"')

connection.close()