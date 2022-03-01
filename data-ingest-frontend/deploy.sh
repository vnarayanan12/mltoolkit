kubectl -n ml-toolkit delete deployment data-ingest-frontend
kubectl apply -f "deployment.yaml"
kubectl apply -f "service.yaml"