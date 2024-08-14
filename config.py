from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

class Config:
    # RabbitMQ
    QUEUE_HOST = getenv('QUEUE_HOST', 'localhost')
    QUEUE_NAME = getenv('QUEUE_NAME')
    # mailtrap
    MAIL_API_URL=getenv('MAIL_API_URL')
    MAIL_API_KEY=getenv('MAIL_API_KEY')
    MAIL_FROM=getenv('MAIL_FROM')
    MAIL_TO=getenv('MAIL_TO')