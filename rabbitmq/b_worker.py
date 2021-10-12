import pika, os, sys, time 

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # if queue running no need to declare queue
    # channel.queue_declare(queue='hello', 
    # needs a new name as rabbitmq doesn't allow redefine an existing queue with different parameters
    channel.queue_declare(queue='task_queue',
                          durable=True)

    def callback(ch, method, properties, body):
        # [x] Received b'Hello World!'
        # The b character in the result prefix signifies it is a byte string 
        # use body.decode('utf-8') to convert it to str.
        print(' [x] Received %r' % body.decode())
        # delays for each dot in body
        time.sleep(body.count(b'.'))
        print(' [x] Done')
        # release memory basic_ack, important!
        # debug: 
        # rabbitmqctl.bat list_queues name messages_ready messages_unacknowledged
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # fair dispath: basic_qos
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue',
                          # auto_ack: redeliver if not consumed
                          # auto_ack=True, # no message acknowledgment with True
                          on_message_callback=callback)

    # waiting for data 
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

'''
round-robin:
By default, RabbitMQ will send each message to the next consumer, in sequence. 
On average every consumer will get the same number of messages. 


'''