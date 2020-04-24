# Kubernetes Lab

> Deploying as an orchestrated Chart with Kubernetes (Minikube) and Helm

## Minikube

* Configure docker to push the docker image in the minikube docker registry instead of local one :
```shell
eval $(minikube -p minikube docker-env)                        
```
It will set following variables :
```shell
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/jberger/.minikube/certs"
export MINIKUBE_ACTIVE_DOCKERD="minikube"
```

*Note :*
> If it is not taken into account (usually when using IDE embedded maven), copy/paste commands above to your shell config file ( eg. ~.bashrc)
>
> Source  the file
>
> Restart your IDE

* Build the micro service using maven :
```shell
mvn clean install
```
It will create the docker image, push it to minikube registry. Then it will build the Helm chart, and install it to minikube, using the just pushed docker image.

* Access your application REST APIs with your browser.

Example : <http://192.168.99.100:8080/hello>
