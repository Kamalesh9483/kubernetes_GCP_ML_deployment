ML Prediction App
This document outlines the process for deploying a Machine Learning prediction application using Docker, Google Cloud Build, Google Container Registry, and Google Kubernetes Engine (GKE).

Steps:
![{EC665809-9E96-4610-9108-B469766E9913}](https://github.com/user-attachments/assets/3991908a-487b-4801-b9c8-d17f43ec384b)

Prediction after deployment:
![image](https://github.com/user-attachments/assets/1b9b1514-9245-403e-8fcd-735192046cb1)


https://github.com/user-attachments/assets/a9339440-ad5f-44c8-a413-de43e6edec9c


## GCP codes:
1. git clone https://github.com/Kamalesh9483/kubernetes_GCP_ML_deployment.git
2. export PROJECT_ID=kubernetes-demo-prediction
3. docker build -t gcr.io/${PROJECT_ID}/price-prediction-app .
4. docker images
5. gcloud auth configure-docker
6. docker push gcr.io/${PROJECT_ID}/price-prediction-app:latest
7. gcloud container clusters create kubernetes-cluster \
    --num-nodes 1 \
    --zone us-central1-a
8. kubectl apply -f deployment.yaml
9. kubectl get pods
10. kubectl apply -f service.yaml
11. kubectl get services


