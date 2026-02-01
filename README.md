# Flipkart Product Returns – Mock API

This project provides a production-style FastAPI mock service exposing
Flipkart product return data with strict validation and pagination.

## Features
- Offset-based pagination (10,000 rows per batch)
- Strict Pydantic schema validation
- Dockerized
- Deployable on Render
- Ready for Airflow / Spark ingestion

## Run Locally
```bash
docker build -t flipkart-mock-api .
docker run -p 8000:8000 flipkart-mock-api
