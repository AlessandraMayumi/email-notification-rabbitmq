> git@github.com:AlessandraMayumi/email-notification-rabbitmq.git

## mailtrap

Integrate with Mailtrap to send emails from your email client through API.

> https://mailtrap.io/home

```sh
curl --location --request POST \
'https://sandbox.api.mailtrap.io/api/send/3078241' \
--header 'Authorization: Bearer ***db8' \
--header 'Content-Type: application/json' \
--data-raw '{"from":{"email":"mailtrap@example.com","name":"Mailtrap Test"},"to":[{"email":"alessandra_mms@hotmail.com"}],"subject":"You are awesome!","text":"Congrats for sending test email with Mailtrap!","category":"Integration Test"}'
```

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
# test email
python client.py
```