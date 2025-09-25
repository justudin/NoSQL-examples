If you’ve \*NOT DONE\* already



* Install Docker Desktop: https://www.docker.com/ 
* Install Anaconda: https://www.anaconda.com/download/success  
* Install/Run Redis: https://redis.io/docs/latest/operate/oss\_and\_stack/install/install-stack/docker 



`docker run -d --name redis -p 6379:6379 redis`



* Install/Run MongoDB: https://www.mongodb.com/resources/products/compatibilities/docker 



`docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server`



* Install/Run Neo4J: https://neo4j.com/docs/operations-manual/current/docker/introduction/ 



`docker run --name neo4j --publish=7474:7474 --publish=7687:7687 --env NEO4J\_AUTH=none neo4j:2025.08.0`







