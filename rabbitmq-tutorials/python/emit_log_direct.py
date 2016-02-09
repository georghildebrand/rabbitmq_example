#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

#We will use a direct exchange instead. The routing algorithm behind a direct exchange is simple
# - a message goes to the queues whose binding key exactly matches the routing key of the message.
channel.exchange_declare(exchange='direct_logs1',
                         durable=True,
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
