from confluent_kafka import Producer
from faker import Faker
import json
import time

fake = Faker()
producer = Producer({'bootstrap.servers': 'kafka:9092'})

def generate_event():
    return {
        "user_id": fake.uuid4(),
        "event_type": fake.random_element(elements=('click', 'view', 'purchase')),
        "event_time": fake.iso8601()
    }

def delivery_report(err, msg):
    if err is not None:
        print('Delivery failed:', err)
    else:
        print('Message delivered to', msg.topic(), msg.partition())

while True:
    event = generate_event()
    producer.produce('events', json.dumps(event), callback=delivery_report)
    producer.poll(0)
    time.sleep(1)
