import pika
import json

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='email_queue')

def send_email_notification(recipient, subject, body):
    message = {
        'recipient': recipient,
        'subject': subject,
        'body': body
    }
    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(message))
    print(" [x] Sent email notification to %s" % recipient)

# Example usage
send_email_notification('test@example.com', 'Test Subject', 'This is a test email body.')

# Close the connection
connection.close()
