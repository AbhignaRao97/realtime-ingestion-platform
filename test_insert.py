from google.cloud import bigquery
from datetime import datetime, timezone

PROJECT_ID = 'realtimeingestion'  # Your actual GCP project ID
DATASET_ID = 'streaming_data'
TABLE_ID = 'events'

client = bigquery.Client(project=PROJECT_ID)

row_to_insert = {
    "user_id": "user_001",
    "event": "login",
    "value": 1,
    "ts": datetime.now(timezone.utc).isoformat()
}

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
errors = client.insert_rows_json(table_ref, [row_to_insert])

if not errors:
    print("✅ Test row inserted successfully!")
else:
    print("❌ Errors occurred:", errors)