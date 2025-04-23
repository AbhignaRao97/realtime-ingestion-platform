# Real-Time Data Ingestion Pipeline with Kafka and BigQuery

This project demonstrates a real-time streaming data pipeline built using **Python**, **Apache Kafka**, and **Google BigQuery**, containerized with **Docker**.

It simulates a producer that streams JSON events into Kafka and a consumer that ingests those events into BigQuery.

---

## ⚙️ Tech Stack
- Python 3.10
- Apache Kafka
- Google BigQuery (via `google-cloud-bigquery`)
- Docker & Docker Compose

---

## 📁 Project Structure

. ├── producer.py # Sends mock data to Kafka ├── consumer.py # Reads from Kafka and inserts to BigQuery ├── main.py # Optional unified consumer logic ├── utils/ │ └── bigquery_writer.py # Helper for BigQuery insertion ├── requirements.txt ├── dockerfile ├── docker-compose.yml ├── architecture.png # Architecture diagram └── README.md

## 🧠 Architecture

![Architecture](architecture.png)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AbhignaRao97/realtime-ingestion-platform.git
cd realtime-ingestion-platform