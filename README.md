# **Chest Cancer Classification Using Deep Learning with MLOps**

![Chest Cancer Classification](https://via.placeholder.com/1000x300?text=Chest+Cancer+Classification+Using+Deep+Learning+with+MLOps)

## **Overview**

This project focuses on the classification of chest cancer using deep learning techniques, particularly Convolutional Neural Networks (CNN). It provides a comprehensive pipeline from data ingestion to model deployment using MLOps practices with tools such as **MLflow**, **DVC**, and **Azure** CI/CD for deployment.

## **Key Features**

- **Deep Learning Model**: A CNN-based model for chest cancer classification using X-ray images.
- **Modular Code Structure**: The project is organized in a modular fashion for better maintainability and scalability.
- **Data Ingestion and Processing**: Efficient data handling using Python scripts for data ingestion and preprocessing.
- **Experiment Tracking**: **MLflow** is used for tracking experiments, logging model parameters, metrics, and artifacts.
- **Model Versioning and Data Management**: **DVC** is implemented for model versioning and handling large datasets.
- **Model Deployment**: The model is deployed as a REST API using a Flask web application.
- **CI/CD with GitHub Actions**: The entire application is dockerized and deployed on **Azure** using a CI/CD pipeline configured via GitHub Actions.

## **Project Structure**

Below is the simplified project structure:

```bash
├── artifacts/
│   └── training/
│       └── model.h5
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_preprocessing.py
│   │   └── model_training.py
│   ├── config/
│   │   └── configuration.py
│   └── utils/
│       └── utilities.py
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
└── .github/
    └── workflows/
        └── azure-deploy.yml
