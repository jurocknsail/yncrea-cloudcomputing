# Getting Started with Maven

[Maven](https://maven.apache.org/what-is-maven.html) provides a simple and fast way to build and deploy applications.

In this course we will use it to automate our development phases.

---

1. **Install Maven**
    
    Well, if you are using a decent IDE, it is already embedded  :thumbsup:
    
    !!! tip
        You may need to add it to your PATH to use outside your IDE ...
    
    Otherwise, you can install it using chocolatey :
    
    ```bash linenums="1"
    choco install maven
    ```

1. **The POM**
    
    This is where all the magic happens ! It is the `xml` file where you can add all the things your app needs to work.
    
    * Dependencies:
        
        The libraries your application need to function. These are called {==dependencies==}.
        
        ````xml linenums="1"
      	<dependencies>
            ...
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
            ...
      	</dependencies>
        ````
      
    * Plugins
    
        Maven is - at its heart - a plugin execution framework. All work is done by {==plugins==}.
        The best idea is to look online for a plugin doing what you want to do.
        
        In our case, we want to build Docker images and create Helm Charts for Kubernetes.
        
        Fortunately, numerous plugins doing such thing are available. We may use :
        
        - [Fabric8 Plugin](https://github.com/fabric8io/fabric8-maven-plugin)
        - [Helm Plugin](https://github.com/kiwigrid/helm-maven-plugin)
        
        They are declared in the pom as following :
        
        !!! warning
            This is just an example, DO NOT change your code right now :)
        
        ````xml linenums="1" hl_lines="5 13 15"
      	<build>
            ...
			<plugin>
				<groupId>com.kiwigrid</groupId>
				<artifactId>helm-maven-plugin</artifactId>
				<version>5.4</version>
				<configuration>
					...
				</configuration>
				<executions>
					<execution>
						<id>helm-package</id>
						<phase>package</phase>
						<goals>
							<goal>package</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
            ...
      	</build>
        ````     
        One important thing to note is that we can {==configure==} plugins.
        
        We can also set when they enter the game in the build by associating them with maven {==phases==}.
        
        And of course, tell the plugin what to do using its own {==goals==}.
        
        !!! tip
            Maven has several phases available, happening in this order :
            ````xml linenums="1"
                <phases>
                  <phase>validate</phase>
                  <phase>initialize</phase>
                  <phase>generate-sources</phase>
                  <phase>process-sources</phase>
                  <phase>generate-resources</phase>
                  <phase>process-resources</phase>
                  <phase>compile</phase>
                  <phase>process-classes</phase>
                  <phase>generate-test-sources</phase>
                  <phase>process-test-sources</phase>
                  <phase>generate-test-resources</phase>
                  <phase>process-test-resources</phase>
                  <phase>test-compile</phase>
                  <phase>process-test-classes</phase>
                  <phase>test</phase>
                  <phase>prepare-package</phase>
                  <phase>package</phase>
                  <phase>pre-integration-test</phase>
                  <phase>integration-test</phase>
                  <phase>post-integration-test</phase>
                  <phase>verify</phase>
                  <phase>install</phase>
                  <phase>deploy</phase>
                </phases>
            ````