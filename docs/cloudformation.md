# Cloudformation Deployment through Github Actions (1 hour)

This exercise is building up on exercise 2.1 (Getting started with AWS).

The goal of this exercise is to automate the deployment of AWS resources once a change to the master branch of a repository occured.

To perform this exercise:

- Add the cloudformation.yaml file from exercise 2.1 in your repository
- Extend your Github Workflow to perform the `aws cloudformation deploy --template-file cloudformation.yaml --stack-name <your-login>-stack` command
