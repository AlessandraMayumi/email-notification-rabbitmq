#!/usr/bin/env python
import pika
from config import Config
from email_client import EmailClient

# Initialize RabbitMQ connection and declare queue
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=Config.QUEUE_HOST)
    )
channel = connection.channel()
channel.queue_declare(queue=Config.QUEUE_NAME, durable=True)

print(' [consumer] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [consumer] Received { body.decode() }, { properties }")
    email_client = EmailClient()
    email_client.send_email()
    print(" [consumer] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=Config.QUEUE_NAME, on_message_callback=callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print(" [consumer] Exiting...")
finally:
    connection.close()
