import pika, os, sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # if queue running no need to declare queue
    # A queue is a buffer that stores messages.
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        # [x] Received b'Hello World!'
        # The b character in the result prefix signifies it is a byte string 
        # use body.decode('utf-8') to convert it to str.
        print(' [x] Received %r' % body)

    channel.basic_consume(queue='hello',
                          auto_ack=True,
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