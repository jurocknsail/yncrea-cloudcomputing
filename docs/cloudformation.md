# CloudFormation Deployment with Github Actions

This exercise is building up on *Getting started with AWS* part.

The goal of this exercise is to automate the deployment of AWS resources once a change to the master branch of a repository occured.

To perform this exercise:

- Add the cloudformation.yaml file from previous lab in your repository
- Extend your Github Workflow to perform :

    ````bash
    aws cloudformation deploy --template-file cloudformation.yaml --stack-name <your-login>-stack
    ````

    !!! success
        Congratulation, you are able to deploy an IaC automaticaly using Github Actions !