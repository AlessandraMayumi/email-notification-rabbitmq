## References
project: git@github.com:AlessandraMayumi/email-notification-rabbitmq.git

message broker: https://www.rabbitmq.com/tutorials/tutorial-two-python

email provider: https://mailtrap.io/home

# Automating Email Notifications with RabbitMQ and Python

This is a study on how to use `RabbitMQ` to send an email notification.

1. Producer:
- Publishes messages to a RabbitMQ queue.
- Uses pika to connect to RabbitMQ.

2. RabbitMQ:
- Acts as a message broker, storing messages in the queue until consumed.

3. Consumer:
- Listens to the RabbitMQ queue.
- Upon receiving a message, it invokes EmailClient to send an email.
- Acknowledges the message after processing.

4. EmailClient:
- Sends an email using the Mailtrap API.
- Configured via Config for API URL, keys, and email details.

## Step-by-Step Execution

1. Start RabbitMQ server if it's not running.
2. Run the consumer script to start listening for messages.
3. Run the producer script to send a test message.

### 1. RabbitMQ server

```sh
# shell 1
docker run -it --rm --name rabbitmq -p 5672:5672 rabbitmq:latest
```

### 2. Consumer
```sh
# shell 2
python consumer.py
```

### 3. Producer
```sh
# shell 3
python producer.py
```

## RabbitMQ

There are several use cases for RabbitMQ, for a general email notification the `Task Queues` is a good fit. Just encapsulate a task as a message and send it to the queue. A worker process running in the background will pop the tasks and eventually execute the job. When you run many workers the tasks will be shared between them.

## mailtrap

Integrate with Mailtrap to send emails from your email client through API.

```sh
curl --location --request POST \
'https://sandbox.api.mailtrap.io/api/send/3078241' \
--header 'Authorization: Bearer ***db8' \
--header 'Content-Type: application/json' \
--data-raw '{"from":{"email":"mailtrap@example.com","name":"Mailtrap Test"},"to":[{"email":"alessandra_mms@hotmail.com"}],"subject":"You are awesome!","text":"Congrats for sending test email with Mailtrap!","category":"Integration Test"}'
```

## Useful commands
```sh
# PYTHON
# create virtual environment
python3 -m venv venv
source venv/bin/activate
# install requirements
pip install -r requirements.txt
# pip freeze
pip freeze > requirements.txt
# DOCKER
docker ps -a
docker stop [CONTAINER_ID]
docker rm [CONTAINER_ID]
```

TODO: Unit Tests
https://dev.to/bshadmehr/testing-rabbitmqconsumerbase-class-l7b
https://github.com/ClearcodeHQ/pytest-rabbitmq/blob/main/tests/test_rabbitmq.py