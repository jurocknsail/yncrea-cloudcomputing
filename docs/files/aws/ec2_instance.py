from troposphere import FindInMap, GetAtt, ImportValue
from troposphere import Output, Ref, Template
from troposphere.ec2 import Tags
from troposphere.autoscaling import LaunchConfiguration,  AutoScalingGroup, Tag as AutoScalingTag

import troposphere.ec2 as ec2

template = Template()

template.add_mapping('RegionMap', {
    "us-east-1": {"AMI": "ami-00b882ac5193044e4"},
    "eu-west-1": {"AMI": "ami-0f62aafc6efe8fd7b"}
})

lc = template.add_resource(LaunchConfiguration(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro"
))

print(template.to_yaml())
