
Now lets build ingest_mongodb image

>> cd mltoolkit/ingestMongoDbDocker
>> docker build -t ingest_mongodb:1.0.0

>> docker tag ingest_mongodb:1.0.0 vnarayanan/ingest_mongodb:1.0.0
>> docker push vnarayanan/ingest_mongodb:1.0.0
Running MongoDB as a Docker Container

docker run -d -p 27017:27017 --name mongodb -d -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo
docker ps
#get the container id and plugin 
docker inspect containerId(mongo)
Get the IP 172.22.0.2 here

###docker run --rm --name example.container example:0.0.1 --file-path=/app/ --mongodb-url=mongodb://root:root@mongo:27017/
  

create C:\data\db
#good one
docker run -it --rm -e MONGODB_CONNSTRING=mongodb://root:root@172.22.0.2:27017 -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ vnarayanan/ingest_mongodb:1.0.0 /bin/bash

#app python ingest_data_docker.py input/ "audio" "files"
View data on mongodb
docker exec -it mongodb /bin/bash
# mongosh
> show databases
> show db.collection
docker stop containerId
docker rm mongodb
_________________________________________________________________________

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
#app:python ingest_data_docker.py input/ "audioFiles" "files"
docker run --name mongodb -d -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\mongodb_data:/data/db -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo
docker run --name mongodb -d -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root mongo

docker run -it --rm -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ -e MONGODB_CONNSTRING=mongodb://root:root@172.17.0.2:27017 ingest_mongodb:1.0.0 /bin/bash

docker run -it --rm -v C:\\Users\\vijin\\kubesamples\\PythonMongoDB\\pythondb\\OutputH5\\:/app/input/ -e MONGODB_CONNSTRING=mongodb://root:root@172.22.0.2:27018 /bin/bash ingest_mongodb:1.0.0 /app/input "audio" "filenames"

View data on mongodb
docker exec -it mongodb /bin/bash
# mongosh
> show databases
> show db.collection
docker stop containerId
docker rm mongodb