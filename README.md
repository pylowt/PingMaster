# PingMaster

## Introduction

**PingMaster** is a simple Python-based microservice that monitors a set of URLs, logs their availability and response time, and stores the results for further analysis. This service is designed to be deployed on Google Cloud Run and is containerised using Docker.

## Planned Features
- Monitor multiple URLs and log their status.
- Configurable ping intervals via a YAML file.
- Logs response times and HTTP status codes.
- Integrated with **CI/CD** pipeline (via GitHub Actions).
- **Infrastructure as code**: Deployed using **Terraform**.
- Simple **local testing** script for developers.

## Planned Tech
This project will be implemented using a variety of technologies and tools. Below is a detailed list of the main components at this stage:
- **Backend**: Python (FastAPI)
- **CI/CD**: GitHub Actions or Cloud Build
- **Cloud**: GCP (Cloud Run)
- **Containerization**: Docker
- **Configuration**: YAML
- **Orchestration**: Proposed out-of-scope improvement, Airflow DAG (for scheduling pings)
- **Logging**: GCP Logs (Proposed out-of-scope improvement, integration with Pub/Sub or Slack)


### Requirements
- Docker
- Terraform
- Python 3.10
- GCP account with Cloud Run enabled

### Run Development Locally

1. Clone this repository and run dev:

```bash
git clone https://github.com/pylowt/PingMaster.git
cd PingMaster/app
fastapi dev main.py
```

## License

MIT License