# Kubernetes Lab

We saw that Docker helps creating Containers. 
Now we need to manage these containers : here comes Kubernetes, the **"Container Orchestrator"**, also called *"K8S"*.

Please visit their [website](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) explaining in details what is K8S ...

In this lab, we will use [Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/) as a local kubernetes, for develoment only.

--- 

## Simple Application Deployment

1. Verify that you can access Kubernetes:  

		kubectl version

	If you see a `Server Version` like below, it means your Kubernetes CLI can connect to your Kubernetes VM:

		$ kubectl version
		Client Version: version.Info{Major:"1", Minor:"13", GitVersion:"v1.13.10", GitCommit:"37d169313237cb4ceb2cc4bef300f2ae3053c1a2", GitTreeState:"clean", BuildDate:"2019-08-19T10:52:43Z", GoVersion:"go1.11.13", Compiler:"gc", Platform:"linux/amd64"}
		Server Version: version.Info{Major:"1", Minor:"13", GitVersion:"v1.13.10", GitCommit:"37d169313237cb4ceb2cc4bef300f2ae3053c1a2", GitTreeState:"clean", BuildDate:"2019-08-19T10:44:49Z", GoVersion:"go1.11.13", Compiler:"gc", Platform:"linux/amd64"}


1. Create the folder `src/kubernetes` in your project.

1. Download the following file to your the newly created folder:  

    -  [deployment.yaml](./files/kubernetes/deployment.yaml)  

1. Open the file in an editor and verify that the `image:` key is referencing your previously built image.

1. Deploy your application with the following command:  

		kubectl apply -f src/kubernetes/deployment.yaml

1. Verify that your application is running properly:  

		kubectl get deployment

   	You shoud now see one running **Pod**, which is scheduled by the **Deployment** that you just created.
   	
   	!!! tip
   	    The number of pods (more specifically, the number of containers) running is displayed in the "READY" column.
   	    
   	    1/1 means 1 container is working fine out of 1 expected, all good :muscle: !

1. You can also check the running Pods in your Kubernetes cluster by typing:  

		kubectl get pods

	This will give a list of running instances (a.k.a. Pods) of your application.
	
	!!! tip
	    Write down the name of the Pod, you'll need it later for reference.

1. In order to access your application, you have to deploy a Kubernetes service.   
Download the following file to your *kubernetes* folder: 

    - [service.yaml](./files/kubernetes/service.yaml) 

    and apply the following command:    

		kubectl apply -f src/kubernetes/service.yaml

1. You have now deployed a so called **NodePort** Kubernetes **Service**. It opens a dedicated port on your Minikube VM, through which you can access the according service.  

    You can find the associated port number by typing:  

		kubectl get svc

    In the example below, the port number would be **30080**:

		$ kubectl get svc  
		
        NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
        kubernetes                  ClusterIP   10.96.0.1        <none>        443/TCP        14d
        yncrea-hellomicro-service   NodePort    10.103.108.153   <none>        80:30080/TCP   2m15s


    !!! info
        If not set in the service, Kubernetes would allow a random NodePort between 30000 and 32767.
            
1. In your browser, open the IP of your Minikube VM (which you retrieved in the docker lab) and add the port that you retrieved from the last command, e.g.: 	[http://minikube-ip:30080](http://minikube-ip:30080).  
   
    !!! success
        You should see "Hello World" example from before, but it's hosted in Kubernetes :thumbsup:.  

---

## Application Scaling

1. Now you'll see the scaling capabilities of Kubernetes. Enter the following command:  

		kubectl.exe scale deployment/yncrea-hellomicro --replicas=3

	With this command, you update the Kubernetes **Deployment** and instruct it to have a total of *three* replicas. 
	
	Kubernetes will handle that by instantiating *two* additional **Pods** to handle more workload.

1. Refresh your browser several times and monitor how the hostname of your microservice changes. 
    
    You may need to use `CTRL + F5`
    
    Kubernetes is loadbalancing your request for you ! 
 
    !!! success
        Congratulations, you just learned how to scale a service in Kubernetes !

---

## Helm Charts

> TODO : Create the chart manaully reusing resource created for simple deployment, no templating

To deploy our containers on kubernetes, we could create k8s objects and deploy them individually as above.


But why not creating a single {==release==} of our microservice deployment, nicely packaged with all the neeeded k8s objects ?
We would then be able to install, upgrade, delete ... any release of our µS, in one single command, with one single package :thinking_face: !

The solution is : **Helm Charts**. Have a look to their awesome [documentation](https://helm.sh/) :face_with_monocle: !

1. Create the Chart

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
    
        Example : <http://192.168.99.100:30080/hello>
