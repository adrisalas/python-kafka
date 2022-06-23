import os
import time
import random

from kafka import KafkaProducer

KAFKA_DEFAULT_SOCKET = "localhost:9092"
KAFKA_DEFAULT_TOPIC = "foobar"


def delay_init():
    time.sleep(10)


def main():
    delay_init()
    kafka_url = os.getenv("KAFKA_SOCKET_ADDRESS", KAFKA_DEFAULT_SOCKET)
    kafka_topic = os.getenv("KAFKA_TOPIC", KAFKA_DEFAULT_TOPIC)

    producer = KafkaProducer(bootstrap_servers=kafka_url)
    while True:
        message = '#{}'.format(random.randint(0, 9999))
        print(f'Sending: {message}', flush=True)
        producer.send(kafka_topic, message.encode()).get(timeout=60)
        time.sleep(random.randint(1, 10))


if __name__ == '__main__':
    main()
