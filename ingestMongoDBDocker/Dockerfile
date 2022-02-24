FROM python:3.6

RUN mkdir -p /app
WORKDIR /app
ADD ingest_mongodb_docker.py /app/.
COPY ingest_mongodb_docker.py /app/.
RUN mkdir /app/input

#COPY ./docker-entrypoint.sh /
RUN pip install --upgrade pip

RUN pip install pymongo
#ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "/app/ingest_mongodb_docker.py"]