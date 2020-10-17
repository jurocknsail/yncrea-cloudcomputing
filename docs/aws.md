# AWS Lab

In this lab, you'll learn :

* How to connect to AWS from your workstation.
* How to design an Infrastructure as Code (IaC) file. 
* How to deploy this file in your Development Environment.

---

## Git Repo for IaC

As mentionned before, we will maintain the IaC in a separated repo.  
Go ahead and create a new **Git Repo** as done before, this time named `yncrea-cloudcomputing-iac`.

!!! info
    From now on, all the IaC files will be pushed to this repo.  
    This way we can {==separate the automation of **infra** deployment and **microservices** deployments==}.
---

## Connect to AWS Educate

1. Go to www.awseducate.com and log in with your Yncréa E-Mail address. You should have already received an invitation.

---

## AWS Connection setup

In this chapter, we'll explain you how to connect with the AWS CLI to your AWS Account.  

1. In the AWS Edcuate console, click on "My Classrooms".

1. In the line of "Cloud Computing", click on "Go to classroom".

1. Confirm with "Continue".

1. In the new window, click on "Account details".

1. In the pop-up window, click on the "Show" button next to "AWS CLI:".

1. Copy and paste the content in the shown box to `%HOME%/.aws/credentials`.

1. Open `%HOME%/.aws/config` and paste 

        [default]
        region = us-east-1
        output = yaml


1. Verify that you have access to the training account:

        aws ec2 describe-instances

    !!! tip
        If you already have other AWS Profiles configured, name them in brackets :
        ````
        [default]
        aws_access_key_id = ...
        aws_secret_access_key = ...

        [other_profile]
        aws_access_key_id = ...
        aws_secret_access_key = ...        
        ````
        And then add the `--profile <profile_name>` to each `aws` commands

---

## VPC

A VPC means Virtual Private Cloud.  
This is what AWS provide us, and we will work inside our own VPC for the rest of this course.

---

## CloudFormation

AWS [CloudFormation](https://aws.amazon.com/cloudformation/?nc1=h_ls) is a YAML based language dedicated to IaC.  
It helps declaring {==ressources==} to define an architecture.

Let's now deploy your first resource in the development account. 
Download the following file to your *IaC Git Repo* in `src/infra` folder.

- [cloudformation.yaml](./files/aws/cloudformation.yaml)  

This file deploys a single EC2 instance.

1. Deploy the EC2 instance with the help of CloudFormation:   

        aws cloudformation deploy --template-file cloudformation.yaml --stack-name <your-login>-stack

1. Wait until the stack is deployed and check if your instance is visible:  

        aws ec2 describe-instances

    !!! success
        Congratulation, you now have access to AWS and can create EC2 machines !

---

## Follow up exercise

Modify the CloudFormation template in order to add a [Security Group](https://docs.aws.amazon.com/fr_fr/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html) which allows access on Port 443 to your EC2 instance.
You can check the result in by verifying the new instance description in the EC2 view.

!!! tip
    Don't forget to also checkout the [EC2 CF Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroups) to know how to assigne the newly SG to the EC2 !

!!! info
    Note that AWS CloudFormation service won't recreate the full stack (if you use the same stack name ofc), but only add the necessary ressources.  
    The feature is called [Stack Update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).    
    It is also smart enough to **restart** the instance {==only if needed !==}  
    (Which is the case here)
    
---

## Troposphere

Another way to generate CloudFormation templates is to use a framework for a programming language. 

One famous example is [Troposphere](https://github.com/cloudtools/troposphere), a Python Framework.  

!!! info
    The advantage of using a framework over bare CloudFormation is that you can use logic, conditions and loops when defining your infrastructure, so in short, it gives more flexibility when building it.  

In this example, we'll generate another EC2 instance.  

Download the following file to your "CloudComputing" folder:  

- [ec2_instance.py](./files/aws/ec2_instance.py)  

After you understood the logic of the file, let's deploy it now.

1. Generate CloudFormation from the Python script:  

        python ec2_instance.py > ec2_instance.yml
        
    !!! warning
        You may need to install python depency : troposphere  
        `pip install troposphere`

1. Deploy the CloudFormation stack:   

        aws cloudformation deploy --template-file ec2_instance.yml --stack-name <your-ldap-login>-ts-stack

    !!! success
        Congratulation, you are able to deploy complex IaC !
        
---

## Follow up exercise

Start from the `ec2_instance.py` file created before and :

- Add the Security Group created before in CF, but this time using Troposphere.
- Package the EC2 Instance in a Launch Configuration that is referenced by an Auto Scaling Group. You can find an example [here](https://github.com/cloudtools/troposphere/blob/master/examples/Autoscaling.py).  
- Add the necessary ressources from the template above to `ec2_instance.py`.
- Generate the yaml from the TS Template `ec2_instance.py`.
- Deploy it.   
- Verify that that your EC2 instance is backed by an Autoscaling group (have a look at the instance tags).
