# CloudFormation with Github Actions - CD

This exercise is building up on *AWS Lab* and *Github Actions Lab* parts.

The goal of this exercise is to automate the deployment of AWS resources once a change to the master branch of a repository occured.

---

To achieve this:

- We are first going to work with the *cloudformation.yaml* file from previous lab.
    
    !!! note
        If you did followup exercise to create the EC2 instance backed with the AutoScaling group, you can use the generated yaml instead.

- Extend your Github Workflow to deploy your stack automatically.  
    The most flexible way is to use the embedded `aws cli` inside the ubuntu image running our actions.
    
    ````bash
    aws cloudformation deploy --template-file src/infra/cloudformation.yaml --stack-name <your-login>-stack
    ````
  
    !!! tip
        Don't forget to [configure the AWS CLI](https://github.com/aws-actions/configure-aws-credentials) before.
        
    !!! success
        Congratulation, you are able to deploy an IaC automaticaly using Github Actions !