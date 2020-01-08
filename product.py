#!/usr/bin/python3
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.10'))
channel = connection.channel()
channel.queue_declare(queue='hello')# creation de la file 

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')# publie   un message 
print(" Message parti ")
connection.close()