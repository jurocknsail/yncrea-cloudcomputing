# What about Docker ?

You may know that Docker is about Containers, so let's start by answering the question : 

*What is a Docker Container ?* by visiting the [Docker site](https://www.docker.com/resources/what-container).

---

## Building & Deploying manually with Docker

The goal here is to Containerize the Spring Boot Microservice we just created.

Then, we are 100% sure that running that way, it will be fine on ANY system ! 

!!! tip
    The best way to avoid the famous "But, it is working on my machine !!"

1. **Create the [Dockerfile](https://docs.docker.com/engine/reference/builder/)**

    - Create the file named `Dockerfile` in the **root directory** of your project, containing :
    
           ````dockerfile linenums="1"
           FROM java:8
           EXPOSE 8080
           ARG JAR_FILE=target/*.jar
           COPY ${JAR_FILE} app.jar
           ENTRYPOINT ["java","-jar","/app.jar"]
           ````
      
        !!! info
            **Line 1** : Our micro service is already embedding Tomcat. All it needs to run is Java, so the image can be based on Java only.
            
            **Line 2** : We want to expose the port 8080 of tomcat to acces our APIs from outside the container.
            
            **Line 3-5** : They are just about putting the build jar to the root of tomcat server, and run it.
            
            > The entrypoint is usually a bash script, or as here, a simple bash command.
        
        
1. **Build the micro service** using maven to get the JAR file ready int the target repository:
    ```shell
    mvn clean package
    ```

1. **Build the docker image** manually
    ```shell
    docker build -t <your_docker_id>/yncrea-hellomicro:latest .
    ```

    It will generate the docker image for the micro service and make it available in the local docker registry.
    The image is tagged as following :
    ```shell
    docker images
   
    REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
    <your_docker_id>/yncrea-hellomicro             latest              b13bcef528c5        46 minutes ago      681MB
    ```
   
1. **Run the image** using Docker CLI :
    ```shell
    docker run -p 8080:8080 -t <your_docker_id>/yncrea-hellomicro:latest
    ```
   Access your application REST APIs with your browser.
   
    Example : <http://minikube-ip:8080/hello> or <http://localhost:8080/hello> when using Docker Desktop. 
    
    !!! tip
        To get the IP of your minikube cluster run the command :
        `minikube ip`
        
        :bulb: You could also set this ip in your {==**hosts**==} file with the name {==**minikube-ip**==} ... 

---

## Building automatically with Maven

**Automatize the build** using Maven Fabric8 plugin :

1. **Find** the latest Fabric8 plugin online
 
    Add the dependency to you pom.

    ??? example "Solution"
        ````xml
        <dependency>
            <groupId>io.fabric8</groupId>
            <artifactId>docker-maven-plugin</artifactId>
            <version>0.33.0</version>
        </dependency>
        ````

1. **Configure** the plugin to build, tag, and push the image to the local docker registry.

    ??? example "Solution"
        ````xml linenums="1" hl_lines="1 2 7 13 14 22 24"
        	<build>
        		<plugins>
        		    ...
        			<plugin>
        				<groupId>io.fabric8</groupId>
        				<artifactId>docker-maven-plugin</artifactId>
        				<configuration>
        					<images>
        						<image>
        							<name>[your_docker_id]/yncrea-hellomicro</name>
        						</image>
        					</images>
        				</configuration>
        				<executions>
        					<execution>
        						<id>docker-build</id>
        						<phase>pre-integration-test</phase>
        						<goals>
        							<goal>build</goal>
        						</goals>
        					</execution>
        				</executions>
        			</plugin>
        		</plugins>
        	</build>
        ````
        
    !!! tip
        You can even use the {=="save" goal==} of the plugin in a new {==execution==}, in order to save the image as a tar file locally.
        
        All this, during the {==maven "pre-integration-test"==} phase :muscle: !  
        
1. **Verify**.
   
    Check your newly built image has been pushed to your local registry (by checking the 'created' time):
   
       ```` shell hl_lines="4"
       docker images
       
       REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
       <your_docker_id>/yncrea-hellomicro             latest              b13bcef528c5        10 seconds ago      681MB

       ````

---

## Cleanup

Now it is time to delete our docker container otherwise we will pollute the next labs.

List all docker container running 
 
```` shell
docker ps
````

Find the ID of the Docker Container you just created and use the first 3 digits of it to stop it :

```` shell
docker stop XYZ
````

You should not see any containers running _yncrea-hellomicro_ image when doing `docker ps`.  
Access your application REST APIs with your browser should __NOT WORK__ anymore.