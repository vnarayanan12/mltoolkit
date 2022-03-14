cd mltookkit/KubeMongoDbPython
docker build -t kube-mongodb:1.0.0 .
Now we can easily use the official mongo Docker image and run it on the same network as the app container.
Run these commands
docker tag and push vnarayanan/kube-mongodb:1.0.0 
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



Notes to know but dont for now -----------------------
If you need to access the MongoDB server from another application running locally, you will need to expose a port using the -p argument.
docker run --name mongodb -d -p 27017:27017 mongo

Any data created as part of the lifecycle of that container will be destroyed once the container is deleted. If you want to persist the data on 
your local machine, you can mount a volume using the -v argument.
docker run --name mongodb -d -v YOUR_LOCAL_DIR:/data/db mongo

If your application is running inside a container itself, you can run MongoDB as part of the same Docker network as your application using --network. With this method, 
you will connect to MongoDB on mongodb://mongodb:27017 from the other containerized applications in the network.
docker run --name mongodb -d --network mynetwork mongo


To initialize your MongoDB with a root user, you can use the environment variables MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD. 
These environment variables will create a user with root permissions with the specified user name and password.

docker run --name mongodb -d -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo

https://www.mongodb.com/compatibility/docker

docker run -d --name MYAPP -e MONGODB_CONNSTRING=mongodb+srv://username:password@clusterURL MYAPP:1.0
docker system prune -a
docker images -f dangling=true
docker image prune
import os
connString = os.environ['MONGODB_CONNSTRING']

If you have an application and a MongoDB container both running on the same machine, you can use Docker Compose to start and stop them together

https://www.mongodb.com/blog/post/running-mongodb-as-a-microservice-with-docker-and-kubernetes

docker run --name mongodb -d -p 27017:27017 -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\mongodb_data:/data/db mongo

docker run -it --rm -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ ingest_mongodb:1.0.0 /bin/bash
"/app/input/" "audioFiles" "files"
docker run --name mongodb -d -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\mongodb_data:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo
docker run --name mongodb -d -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo

docker run -it --rm -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ -e MONGODB_CONNSTRING=mongodb://root:root@172.17.0.2:27017 ingest_mongodb:1.0.0 /bin/bash

docker run -it --rm -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ -e MONGODB_CONNSTRING=mongodb://root:root@172.17.0.2:27017 ingest_mongodb:1.0.0 /app/input "audio" "filenames"

View data on mongodb
docker exec -it mongodb /bin/bash
# mongosh
> show databases
> show db.collection
docker stop containerId
docker rm mongodb

Source
https://levelup.gitconnected.com/deploy-your-first-flask-mongodb-app-on-kubernetes-8f5a33fa43b4
