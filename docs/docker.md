# What about Docker ?
> TODO : Quick intro using their doc ....

# Deploying as a simple Container with Docker

The goal here is to Dontainerize the Spring Boot Microservice we just created using Docker.

1. Create the Dockerfile
    >TODO

1. Build the micro service using maven to get the JAR file ready int the target repository:
    ```shell
    mvn clean package
    ```

1. Build the docker image manually
    ```shell
    cd docker
    docker build -t <your_docker_id>/yncrea-hellomicro:latest .
    ```

    It will generate the docker image for the micro service and make it available in the local docker registry.
    The image is tagged as following :
    ```shell
    REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
    <your_docker_id>/yncrea-hellomicro             latest              b13bcef528c5        46 minutes ago      681MB
    ```
   
1. Run the image using Docker CLI :
    ```shell
    docker run -p 8080:8080 -t <your_docker_id>/yncrea-hellomicro:latest
    ```
   Access your application REST APIs with your browser.
   
   Example : <http://localhost:8080/hello>

1. Automatize the **build** using Maven Fabric8 plugin :
    > TODO
