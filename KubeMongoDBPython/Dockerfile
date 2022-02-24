FROM python:alpine3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN mkdir /app/input

ENV PORT 5000
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["ml-toolkit.py"]