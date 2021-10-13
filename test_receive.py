import pika
import sys

#指定远程rabbitmq的用户名密码
username = 'guest'
pwd = 'guest'
user_pwd = pika.PlainCredentials(username, pwd)

#创建连接
s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=user_pwd))

#在连接上创建一个频道
channel = s_conn.channel()

# 声明exchange的类型为模糊匹配，这里设置交换为持久化的
channel.exchange_declare(exchange='amq.topic',exchange_type='topic', durable=True)  

# 创建随机一个队列当消费者退出的时候，该队列被删除。
result = channel.queue_declare(queue='', exclusive=True)

# 创建一个随机队列名字。  
queue_name = result.method.queue

#绑定键。‘#’匹配所有字符，‘*’匹配一个单词。这里列表中可以为一个或多个条件，能通过列表中字符匹配到的消息，消费者都可以取到
binding_keys = ['RPi.Data']

#通过循环绑定多个“交换机-队列-关键字”，只要消费者在rabbitmq中能匹配到与关键字相应的队列，就从那个队列里取消息
for binding_key in binding_keys:
    channel.queue_bind(exchange='amq.topic',
                       queue= queue_name,
                       routing_key=binding_key)

#设置callback等，其中不给rabbitmq发送确认
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

#开始循环接收消息
print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()