# Kafka Spark Streaming Pipeline (Dockerized)

A real-time data processing pipeline using Apache Kafka, Spark Structured Streaming, and Python — fully containerized with Docker.

## 📦 Components

- **Kafka**: Broker for real-time stream ingestion
- **Producer**: Python-based, generates events with `faker`
- **Spark**: Consumes events, processes, and writes metrics to Parquet
- **Output**: Parquet files + checkpoints

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/kafka-spark-pipeline.git
cd kafka-spark-pipeline
```

### 2. Build & Run the Pipeline
```bash
docker-compose up --build
```

This will start Zookeeper, Kafka, the Python producer, and Spark job in containers.

### 3. Output Directory
- Parquet Files: `output/metrics/`
- Checkpoints: `output/checkpoint/`

---

## 🔍 Tech Stack

- Python (Producer)
- Apache Kafka (Docker)
- Apache Spark Structured Streaming (PySpark)
- Parquet Storage
- Docker Compose

---

## 📝 License
MIT
