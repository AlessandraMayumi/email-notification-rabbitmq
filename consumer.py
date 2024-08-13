import pika
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# Function to send an email
def send_email(recipient, subject, body):
    # Replace these with your email provider's SMTP settings
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    
    sender_email = 'your_email@example.com'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient} with subject '{subject}'")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='email_queue')

def callback(ch, method, properties, body):
    message = json.loads(body)
    recipient = message['recipient']
    subject = message['subject']
    body = message['body']
    send_email(recipient, subject, body)

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
