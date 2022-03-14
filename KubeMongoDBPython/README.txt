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

>>curl 10.107.107.36:8080/audio
curl 10.96.21.73:8080
>>
curl -X POST -d "{\"audio_files\": \"File 1\"}" 10.107.107.36:8080/audio_file
curl -X POST -d "{\"task\": \"Task 3\"}" http://10.96.21.73:8080/task
curl -X POST -d "{\"audiofile\": \"File 2\"}" http://10.96.21.73:8080/audiofile

curl -X POST -d "{\"audiofile\": \"File 1\"}" http://10.96.21.73:8080/audiofile

kubectl port-forward svc/mongo 27017:27017

 kubectl exec -it mongo-5cc97976c-bv6kg /bin/bash
mongo --port 27018 --username XXXX --password XXXX

Source
https://levelup.gitconnected.com/deploy-your-first-flask-mongodb-app-on-kubernetes-8f5a33fa43b4
