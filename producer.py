from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

topic_name = 'event_stream'

print("⚙️ Starting Kafka Producer...")

try:
    # Connect to Kafka broker
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',  # Use '127.0.0.1:9092' if localhost doesn't work
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print(f"✅ Connected to Kafka broker at localhost:9092")
except Exception as e:
    print("❌ Failed to connect to Kafka:", e)
    exit(1)

# Simulate and send mock data
try:
    print(f"📤 Sending messages to Kafka topic: '{topic_name}'")
    while True:
        message = {
            "user_id": f"user_{random.randint(1, 100)}",
            "event": random.choice(["login", "logout", "purchase", "click"]),
            "value": random.randint(1, 100),
            "ts": datetime.utcnow().isoformat()
        }
        print(f"🔄 Sending: {message}")
        producer.send(topic_name, message)
        time.sleep(2)
except Exception as err:
    print("❌ Error while sending message:", err)