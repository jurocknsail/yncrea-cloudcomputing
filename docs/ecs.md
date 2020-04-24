# Deploy Containers with ECS

This exercise is building up on exercise 1.4 (Github Actions).

The goal of this exercise is to deploy your previously built Docker image to the public Docker hub: hub.docker.com

First, deploy an ECS cluster with Cloudformation from the following file:

- [ecs-cluster.yaml](./files/aws/ecs-cluster.yaml)
    - Choose the default security group, VPC and all subnets

The goal of this exercise is to extend your your Github Actions to:

- Add the following file to your repository
    - [ecs-task.yaml](./files/aws/ecs-task.yaml)
- Extend your Github flow with the following lines:

        aws cloudformation deploy --template-file ecs-task.yaml --stack-name ecs-task --parameter-overrides ImageName=docker.io/<your-docker-username>/ssc:sha-$(git rev-parse --short HEAD) --no-fail-on-empty-changeset
