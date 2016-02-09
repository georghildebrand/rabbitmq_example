#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# if no queue is bound to an exchange all messages will be lost
channel.exchange_declare(exchange='logs',
                         type='fanout')
# once we disconnect the consumer the queue should be deleted.
# There's an exclusive flag for that:
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# A binding is a relationship between an exchange and a queue.
# This can be simply read as: the queue is interested in messages from this exchange.
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
