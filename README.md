# Twitter ETL Pipeline using Apache Airflow

🚀 An end-to-end ETL pipeline that extracts tweets using Twitter (X) API, processes the data, and loads it into AWS S3 using Apache Airflow.

## 🔧 Tech Stack
- Apache Airflow 2.9
- Python 3.12
- Tweepy (Twitter API v2)
- Pandas
- AWS S3
- AWS EC2 (Ubuntu 24.04)

## 📌 Architecture
1. **Extract**: Fetch recent tweets using Tweepy
2. **Transform**: Clean and structure tweet data using Pandas
3. **Load**: Upload transformed data to AWS S3
4. **Orchestration**: Airflow DAG scheduled daily

## 📂 Project Structure
dags/
└── twitter_dag.py
etl/
└── twitter_etl.py


## ▶️ How to Run
1. Create a Python virtual environment
2. Install dependencies
   ```bash
   pip install -r requirements.txt

export TWITTER_BEARER_TOKEN=your_token
airflow scheduler
airflow webserver
