import os
import time

from kafka import KafkaConsumer

KAFKA_DEFAULT_SOCKET = "localhost:9092"
KAFKA_DEFAULT_TOPIC = "foobar"


def delay_init():
    time.sleep(10)


def main():
    delay_init()
    kafka_url = os.getenv("KAFKA_SOCKET_ADDRESS", KAFKA_DEFAULT_SOCKET)
    kafka_topic = os.getenv("KAFKA_TOPIC", KAFKA_DEFAULT_TOPIC)
    consumer = KafkaConsumer(kafka_topic,
                             group_id='foo',
                             bootstrap_servers=[kafka_url])
    try:
        while True:
            consume_messages(consumer)
    finally:
        consumer.close()


def consume_messages(consumer):
    raw_messages = consumer.poll(timeout_ms=1000, max_records=5000)
    if not raw_messages:
        time.sleep(5)
    for topic_partition, messages in raw_messages.items():
        for message in messages:
            print(f'Consumed: {message.value.decode()}', flush=True)


if __name__ == '__main__':
    main()
