cd mltookkit/KubeMongoDbPython
docker build -t kube-mongodb:1.0.0 .
Now we can easily use the official mongo Docker image and run it on the same network as the app container.
Run these commands
docker tag kube-mongodb:1.0.0 vnarayanan/kube-mongodb:1.0.0
docker push vnarayanan/kube-mongodb:1.0.0  
>docker network create mltoolkit-net
>docker run --name=mongo --rm -d --network=mltoolkit-net mongo
>docker run –-name=kubemongo --rm -p 5000:5000 -d –-network=mltoolkit-net vnarayanan/kube-mongodb:1.0.0

minikube start
minikube status

kubectl apply -f kube-mongodb.yaml
kubectl get pods -o wide
kubectl get services
Create persistent volume
kubectl apply -f kube-mongodb-pv.yaml

kubectl apply -f kube-mongodb-pvc.yaml

The mongo.yaml, similar to the kube-mongodb.yaml, is where we define the mongo deployment that creates a single instance of MongoDB server. Here, 
we expose the port 27017 which can be accessed by other pods. The persistent volume claimed can be mounted onto a directory on the container.

kubectl apply -f mongo.yaml

This service makes the mongo pod accessible from within the cluster, 
but not from outside. The only resource that should have access to the MongoDB database is our app.
Here, the port 27017 of the service mongo-svc is bound to the port 27017 of the mongo pod attached to it.

kubectl get svc mongo
>> minikube ssh
$$ curl IP:27017 to see if you can access
Result
It looks like you are trying to access MongoDB over HTTP on the native driver port.

>>curl 10.107.107.36:8080/tasks
curl 10.96.21.73:8080/tasks
curl 10.96.21.73:8080/audio
>>
curl -X POST -d "{\"audio_files\": \"File 1\"}" 10.107.107.36:8080/audio_file
curl -X POST -d "{\"task\": \"Task 3\"}" http://10.96.21.73:8080/task
curl -X POST -d "{\"audiofile\": \"File 3\"}" http://10.96.21.73:8080/audiofile

curl -X POST -d "{\"task\": \"File 2\"}" http://10.96.21.73:8080/task

kubectl port-forward mongopodxxx 27017

https://www.mongodb.com/try/download/shell download mongosh

kubectl exec -it mongo-5cc97976c-bv6kg /bin/bash
#mongo

mongo --port 27018 --username XXXX --password XXXX

Let’s try and access the database from outside the cluster. In order to do so, we must create another Kubernetes Service.
kubectl create -f mongodb-nodeport-svc.yaml

To connect from outside the Kubernetes cluster, you must use the Kubernetes cluster’s worker node IP address or a load balancer address. In case you are following on Minikube, you can use minikube’s IP to connect.
To see minikube IP or service URLs, use the following commands
minikube ip

192.168.49.2

minikube service --url mongo-nodeport-svc

Command to conenct
kubectl exec -it mongo-5cc97976c-bv6kg /bin/bash

mongo --host 192.168.49.2 --port 27017 -u adminuser -p password123

kubectl apply -f mongo-client.yaml
kubectl exec deployment/mongo-client -it -- /bin/bash
mongo --host mongo-nodeport-svc --port 27017 
show dbs
use dev
show collections
db.task.find()


Source
https://levelup.gitconnected.com/deploy-your-first-flask-mongodb-app-on-kubernetes-8f5a33fa43b4
