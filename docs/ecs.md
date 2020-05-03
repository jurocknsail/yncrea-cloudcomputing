# Deploy Containers with ECS

The goal of this exercise is to deploy your previously built Docker image automatically to the AWS container service : ECS.

- First, deploy an ECS cluster with CloudFormation from the following file: 
    - [ecs-cluster.yaml](./files/aws/ecs-cluster.yaml)
    - Choose the default security group, VPC and all subnets

- Add the following file to your repository
    - [ecs-task.yaml](./files/aws/ecs-task.yaml)

- Extend your Github flow with the following lines:

        aws cloudformation deploy --template-file ecs-task.yaml --stack-name ecs-task --parameter-overrides ImageName=docker.io/<your-docker-username>/ssc:sha-$(git rev-parse --short HEAD) --no-fail-on-empty-changeset
