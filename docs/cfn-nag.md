# Cloudformation Linting

As you saw in the presentation, all layers of your application must be properly secured.   
This what we call **Defense in Depth**.  

The lowest layer in a public cloud deployment is the {==infrastructure==} and in the case of AWS, we are deploying it through CloudFormation.  
There can be very common pitfalls when it comes to Infrastructure as Code, so it can be very advantageous to automate the scan for these.

One very known tools is **[cfn-nag](https://github.com/stelligent/cfn_nag)**.  

- Install Ruby:

        choco install ruby

- Install `cfn_nag`:

        gem install cfn-nag

- Scan the following file using `cfn_nag_scan` :

    - [cf-all.yaml](./files/aws/cf-all.yaml)
    
- Fix all issues that are reported through the scanner.

---

There is already a Github Action available for this tool [here](https://github.com/marketplace/actions/stelligent-cfn_nag).  

- Integrate this lint program into your Github workflow and do the validation of your CF files before you actually deploy the resources in AWS.

    !!! success
        Congratulation, you are now able to validate your IaC before deploying it !