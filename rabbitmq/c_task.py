import pika, sys

# broker: localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# send the message to quene
# durable to make sure messages aren't lost 
channel.queue_declare(queue='task_queue',
                      durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World!'

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      prroperties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      ))
print(' [x] Sent %r ' % message)

connection.close()