# **Chest Cancer Classification using Deep Learning and MLOps**

![Chest Cancer Classification](https://via.placeholder.com/1000x300?text=Chest+Cancer+Classification+using+Deep+Learning+and+MLOps)

## **Overview**

This project aims to classify chest cancer from X-ray images using deep learning techniques. It demonstrates an end-to-end workflow for deploying a machine learning model using MLOps tools and practices. The project incorporates model training, evaluation, and deployment using tools like **MLflow**, **DVC**, **BentoML**, and **Azure CI/CD pipelines**.

## **Key Features**

- **Deep Learning Model**: Utilizes Convolutional Neural Networks (CNN) for accurate image classification.
- **Data Version Control**: Efficient management of data versions using **DVC**.
- **Experiment Tracking**: Models and their parameters are tracked using **MLflow**.
- **Modular Code Structure**: Implements modular coding practices for scalability and maintainability.
- **Model Serving and Deployment**: Uses **BentoML** for packaging and serving the model, deployed on **Azure** via **CI/CD pipelines**.
- **Dockerized Application**: Containerization of the Flask app for a consistent and portable deployment environment.

## **Project Architecture**

Below is a simplified overview of the project structure:

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
