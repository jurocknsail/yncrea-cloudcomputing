# Hello Microservice

An amazing test micro-service using Java Spring Boot for the "Intro to Cloud Computing" course purpose.

It does basically ... nothing :)

---

## Prerequisites
* Having a Github account
* Having Docker installed
* Having Helm installed
* Having a Kubernetes cluster ready (Minikube fits perfectly for local development)

---

## Deploying as a simple Container with Docker

* Configure docker to push the docker image in the local docker registry (default behavior) :
```shell
eval "$(docker-machine env -u)"
```
It will unset following variables in case they were set custom values :
```shell
unset DOCKER_TLS_VERIFY
unset DOCKER_HOST
unset DOCKER_CERT_PATH
unset DOCKER_MACHINE_NAME
```

*Note :*
> If it is not taken into account (usually when using IDE embedded maven), copy/paste commands above to your shell config file ( eg. ~.bashrc)
>
> Source  it
>
> Restart your IDE

* Build the micro service using maven :
```shell
mvn clean package
```
It will generate the docker image for the micro service and make it available in the local docker registry.
The image is tagged as following :
```shell
REPOSITORY                                TAG                 IMAGE ID            CREATED             SIZE
jurocknsail/yncrea-hellomicro             latest              b13bcef528c5        46 minutes ago      681MB
```

* Use docker CLI to run it : 
```shell
docker run -p 8080:8080 -t yncrea/hellomicro:latest
```

* Access your application REST APIs with your browser.

Example : <http://localhost:8080/hello>

---

## Deploying as an orchestrated Chart with Kubernetes and Helm

### Minikube

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
<br/><br/>

### AWS EKS Cluster  

*To be continued ...*

---

## Integrations
Slack notifications using [ voxmedia/github-action-slack-notify-build ](https://github.com/voxmedia/github-action-slack-notify-build) for the maven build.
> Scopes used are :
>
> chat:write
>
> channels:read
>
> groups:read