# kubernetes_GCP_ML_deployment

## Steps:
1. git clone https://github.com/Kamalesh9483/kubernetes_GCP_ML_deployment.git
2. export PROJECT_ID=kubernetes-demo
3. gcloud builds submit --tag gcr.io/${PROJECT_ID}/price-prediction-app .
4. gcloud container clusters create kubernetes-cluster \
    --num-nodes 1 \
    --enable-basic-auth \
    --issue-client-certificate \
    --zone us-central1-a
5. kubectl apply -f deployment.yaml
6. kubectl get pods
7. kubectl apply -f service.yaml
8. kubectl get services

