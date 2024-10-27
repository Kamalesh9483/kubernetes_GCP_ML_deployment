# kubernetes_GCP_ML_deployment

## Steps:
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


