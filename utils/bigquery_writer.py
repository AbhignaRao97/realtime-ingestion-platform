from google.cloud import bigquery
import logging

PROJECT_ID = '6826-7058-4002'
DATASET_ID = 'your_dataset'
TABLE_ID = 'your_table'

bq_client = bigquery.Client(project=PROJECT_ID)

def write_to_bigquery(data):
    errors = bq_client.insert_rows_json(f"{DATASET_ID}.{TABLE_ID}", [data])
    if errors:
        logging.error(f"BigQuery insertion errors: {errors}")
    else:
        logging.info("Data written to BigQuery")