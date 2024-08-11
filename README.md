**Built and Dockerized Python Factorial App, Deployed to Docker Hub**

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
*Check Whether Docker is Working Properly by Running hello-world*
![ss1](https://github.com/Vijay-KV09/Docker/blob/master/Screenshot%20(35).png)
*Clone The Respo from GitHub Where Dockerfile and Python App is Deployed*
```bash
git clone https://github.com/Vijay-KV09/Docker  
```
---
*Check Whether The Dockerfile and Python File is seen in Docker Images*
![ss2](https://github.com/Vijay-KV09/Docker/blob/master/Screenshot%20(29).png)
*After Successfully Image is Seen in Docker Images build the Docker Image* 
```bash
docker build -t docker1 .
```
