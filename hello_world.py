#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 08.02.2016

@author: ghildebrand
'''

if __name__ == '__main__':
    import pika
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   '0.0.0.0'))
    channel = connection.channel()
    #declare a queue
    channel.queue_declare(queue='hello')
