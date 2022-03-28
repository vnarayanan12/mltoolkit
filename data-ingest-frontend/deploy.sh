kubectl -n ml-toolkit delete deployment data-ingest-frontend-deployment
kubectl -n ml-toolkit delete service data-ingest-frontend-service
kubectl -n ml-toolkit delete ingress data-ingest-frontend-ingress
kubectl apply -f "deployment.yaml"
kubectl apply -f "service.yaml"
kubectl apply -f "data-ingest-frontend-ingress.yaml"