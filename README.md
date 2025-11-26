# End-to-end Machine Learning Project with MLflow, Streamlit, Docker, and AWS CI/CD

This repository provides a complete end-to-end machine learning workflow, including data pipelines, ML experiments, model tracking, a Streamlit-based prediction UI, Docker containerization, and automated CI/CD deployment to AWS using GitHub Actions.

---

# Project Workflow

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update entity definitions
5. Update configuration manager (`src/config`)
6. Update ML pipeline components
7. Update pipeline orchestrator
8. Update `main.py`
9. Update `streamlit_app.py` (Streamlit UI)

---

# How to Run Locally

## 1. Clone the repository

```
git clone https://github.com/Roshan-RB/end-to-end_ML_with_MLflow
cd end-to-end_ML_with_MLflow
```

## 2. Create and activate a virtual environment

```
conda create -n mlproj python=3.11 -y
conda activate mlproj
```

## 3. Install project requirements

```
pip install -r requirements.txt
```

## 4. Run the ML training pipeline

```
python main.py
```

## 5. Run the Streamlit application

```
streamlit run streamlit_app.py
```

Open the application in your browser at:

```
http://localhost:8501
```

---

# MLflow Tracking

Start MLflow UI locally:

```
mlflow ui
```

Access the UI at:

```
http://127.0.0.1:5000
```

Optional integration with DagsHub:

```
import dagshub
dagshub.init(
    repo_owner='Roshan-RB',
    repo_name='end-to-end_ML_with_MLflow',
    mlflow=True
)
```

---

# Docker Support

## Build the Docker image

```
docker build -t wine-ml-app .
```

## Run the Docker container

```
docker run -p 8501:8501 wine-ml-app
```

Access the application at:

```
http://localhost:8501
```

---

# AWS CI/CD Deployment (ECR, EC2, GitHub Actions)

This project includes a complete AWS deployment pipeline using GitHub Actions.

## Required AWS Services

* ECR (Elastic Container Registry)
* EC2 (Ubuntu instance)
* IAM (user with programmatic access)

---

# IAM Permissions

Attach the following AWS managed policies to your deployment IAM user:

* AmazonEC2ContainerRegistryFullAccess
* AmazonEC2FullAccess

---

# Create an ECR Repository

Example ECR URI format:

```
123456789012.dkr.ecr.eu-central-1.amazonaws.com/mlproject
```

Region used: `eu-central-1` (Frankfurt)

---

# EC2 Setup

1. Launch an Ubuntu EC2 instance.
2. Install Docker:

```
sudo apt update -y
sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

# Configure EC2 as a GitHub Self-hosted Runner

Navigate to GitHub:

```
Repository Settings → Actions → Runners → New self-hosted runner
```

Follow the setup steps provided.

---

# GitHub Secrets Required

Set the following secrets:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_REGION = eu-central-1
* AWS_ECR_LOGIN_URI (example: 123456789012.dkr.ecr.eu-central-1.amazonaws.com)
* ECR_REPOSITORY_NAME (example: mlproject)

---

# CI/CD Pipeline Summary

The GitHub Actions workflow performs the following steps:

1. Linting and unit tests
2. Build Docker image
3. Push Docker image to ECR
4. Pull image on EC2
5. Stop existing container (if any)
6. Deploy the new container
7. Clean up unused Docker resources

The final container runs on EC2 and serves the Streamlit application on port 8501.

---

# Technologies Used

* Streamlit
* MLflow
* Docker
* GitHub Actions
* AWS ECR and EC2
* DagsHub (optional)
* Scikit-learn
* Python 3.11
* Pandas and NumPy

---


