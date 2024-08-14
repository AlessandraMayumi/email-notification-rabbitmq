#!/usr/bin/env python
import pika
from config import Config

# Initialize RabbitMQ connection and declare queue
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=Config.QUEUE_HOST)
    )
channel = connection.channel()
channel.queue_declare(queue=Config.QUEUE_NAME, durable=True)

# Publish message
channel.basic_publish(
    exchange='',
    routing_key= Config.QUEUE_NAME,
    body="Hello World!",
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # Make message persistent
    ))

print(" [producer] Sent message")
connection.close()
