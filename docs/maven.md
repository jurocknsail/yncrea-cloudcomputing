# Maven Lab

[Maven](https://maven.apache.org/what-is-maven.html) provides a simple and fast way to build and deploy applications.

In this course we will use it to automate our development phases.

1. Install Maven
    
    Well, if you are using a decent IDE, it is already embedded  :thumbsup:
    
    !!! tip
        You may need to add it to your PATH to use outside your IDE ...
    
    Otherwise, you can install it using chocolatey :
    
    ```bash linenums="1"
    choco install maven
    ```

1. The POM
    
    This is where all the magic happens ! It is the `xml` file where you can add all the things your app needs to work.
    
    * Dependencies:
        
        The libraries your application need to function. These are called {==dependencies==}.
        
        ````xml linenums="1"
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        ````
      
    * Plugins
    
        > TODO
    
    * Phases
        
        > TODO
    
    * Goals
    
        > TODO
    
    