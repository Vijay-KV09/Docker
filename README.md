**Deploying Python Mini Application Into Docker Conatiners and Managing in Docker Hub**
---
Steps=>

1: Create EC2 instance on AWS

2: Using Linux install Docker on the EC2

3: Update all the packages of Linux

4: Clone github repo where Docker file and python file is located

5: Give Access to User to get Controlled by Docker Daemon

6: Build the Docker image using the Docker File

7: Run the Docker image using Docker run commad (docker run image:latest)

8: After Successful Execution tag the docker image with the repo created for storing image

9: Push the image to the Docker Hub

10: To Execute the image again just pull the image from the Docker Hub

**After Successful Installing the Docker On EC2**
---
Run The Following Command in Order:

1: sudo apt install docker.io  

2: sudo systemctl status docker

3: docker run hello-world

*"After this {Restart} the server"*

4: sudo systemctl status docker

5: sudo usermod -aG docker ubuntu

6: git clone https://github.com/Vijay-KV09/Docker

7: docker build -t docker1 .

8: docker run -e N=15 docker1

9: docker images

10: docker login 

*"Authenticate docker hub using username and password and Create a repo for storing the docker image in docker hub"*

11: docker tag docker1 dockerhub-username/repository-name:tag

12: docker push dockerhub-username/repository-name:tag

**Hence You Deployed Your First Docker Image In Your Registry**
