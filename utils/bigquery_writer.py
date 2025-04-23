from google.cloud import bigquery
import os
import csv

def write_to_bigquery(project_id, dataset_id, table_id, data):
    client = bigquery.Client(project=project_id)

    csv_file = "temp_data.csv"
    fieldnames = list(data.keys())

    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        schema=[
            bigquery.SchemaField("user_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("event", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("value", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("ts", "TIMESTAMP", mode="REQUIRED"),
        ],
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    with open(csv_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        job.result()

    print("✅ Batch loaded into BigQuery from CSV.")