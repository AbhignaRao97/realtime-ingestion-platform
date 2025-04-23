from kafka import KafkaConsumer
import json
from utils.bigquery_writer import write_to_bigquery

# Set project details
PROJECT_ID = "realtimeingestion"
DATASET_ID = "streaming_data"
TABLE_ID = "events"

print("📥 Starting Kafka Consumer...")

consumer = KafkaConsumer(
    'event_stream',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print(f"✅ Subscribed to topic 'event_stream'")

for message in consumer:
    data = message.value
    print(f"🔄 Received from Kafka: {data}")
    write_to_bigquery(PROJECT_ID, DATASET_ID, TABLE_ID, data)
print(f"✅ Subscribed to topic 'event_stream'")

for message in consumer:
    data = message.value
    print(f"🔄 Received from Kafka: {data}")
    write_to_bigquery(PROJECT_ID, DATASET_ID, TABLE_ID, data)