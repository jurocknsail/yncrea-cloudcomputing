# Kubernetes Lab

> Deploying as an orchestrated Chart with Kubernetes (Minikube) and Helm
## Helm Charts
> TODO : A quick overview using their doc ...

## Minikube

1. Create the Chart archive

    > TODO

1. Deploy the Chart to Minikube using Helm

    > TODO

1. Automatize using Maven Helm plugin :

    > TODO

    ```shell
    mvn clean install
    ```
    It will create the docker image, push it to minikube registry. Then it will build the Helm chart, and install it to minikube, using the just pushed docker image.
    
    * Access your application REST APIs with your browser.
    
        Example : <http://192.168.99.100:8080/hello>
