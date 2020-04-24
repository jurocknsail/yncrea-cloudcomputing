# Cloudformation Linting (1 hour)

As you saw in the presentation, all layers of your application must be properly secured. This what we call **Defense in Depth**.

The lowest layer in a public cloud deployment is the infrastructure and in the case of AWS, we are deploying it through CloudFormation. There can be very common pitfalls when it comes to Infrastructure as Code, so it can be very advantageous to automate the scan for these.

One very known tools is **cfn-nag**. There is already a Github Action available for this tool [here](https://github.com/marketplace/actions/cfn-nag-action). 

Please scan the following file:

- [cf-all.yaml](./files/aws/cf-all.yaml)

In this exercise, integrate this lint program into your Github workflow and do the validation before you actually deploy resources in AWS. Also, fix all issues that are reported through the scanner.