# Deploying as a simple Container with Docker

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
