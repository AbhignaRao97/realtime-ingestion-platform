from kafka import KafkaConsumer
from utils.bigquery_writer import write_to_bigquery
import json
import logging

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    'realtime-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='ingestion-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    logging.info(f"Received: {data}")
    write_to_bigquery(data)