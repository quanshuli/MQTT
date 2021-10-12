'''
Remote Procedure Call or RPCc

Make sure it's obvious which function call is local and which is remote.
Document your system. Make the dependencies between components clear.
Handle error cases. How should the client react when the RPC server is down for a long time?

When in doubt avoid RPC. 
If you can, you should use an asynchronous pipeline - instead of RPC-like blocking, 
results are asynchronously pushed to a next computation stage.
'''
import pika

connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
                     
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()