ng build --output-path=./dist/data-ingest-frontend
docker build -t data-ingest-frontend:1.0 .
docker tag data-ingest-frontend:1.0 gbrown97/data-ingest-frontend:1.0
docker push gbrown97/data-ingest-frontend:1.0