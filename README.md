GitHub repo: git@github.com:AlessandraMayumi/email-notification-rabbitmq.git

## RabbitMQ

Run RabbitMQ server

```sh
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:latest
```

## Run Your Scripts

- Producer (Email Sender)
- Consumer (Email Processor)

1. Start RabbitMQ server if it's not running.
2. Run the consumer script to start listening for messages.
3. Run the producer script to send a test message.

## Development
```sh
pip freeze > requirements.txt
```