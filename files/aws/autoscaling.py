from troposphere import Parameter, Ref, Template, FindInMap
from troposphere.autoscaling import AutoScalingGroup, Tag
from troposphere.autoscaling import LaunchConfiguration
from troposphere.policies import (
    AutoScalingReplacingUpdate, AutoScalingRollingUpdate, UpdatePolicy
)
import troposphere.ec2 as ec2


t = Template()

t.set_description("""\
Configures autoscaling group for api app""")

SecurityGroup = t.add_parameter(Parameter(
    "SecurityGroup",
    Type="String",
    Description="Security group name.",
    Default="my-ingress-group"
))

ScaleCapacity = t.add_parameter(Parameter(
    "ScaleCapacity",
    Default="3",
    Type="String",
    Description="Number of api servers to run",
))

AmiId = t.add_parameter(Parameter(
    "AmiId",
    Type="String",
    Description="The AMI id for the api instances",
    Default="ami-00b882ac5193044e4"
))

t.add_mapping('RegionMap', {
    "us-east-1": {"AMI": "ami-00b882ac5193044e4"},
    "eu-west-1": {"AMI": "ami-0f62aafc6efe8fd7b"}
})

# Define the instance security group
instance_sg = t.add_resource(
    ec2.SecurityGroup(
        "InstanceSecurityGroup",
        GroupDescription="Enable 443 inbound port",
        GroupName=Ref(SecurityGroup),
        SecurityGroupIngress=[
            ec2.SecurityGroupRule(
                IpProtocol="tcp",
                FromPort="443",
                ToPort="443",
                CidrIp="0.0.0.0/0",
            )
        ]
    )
)

# Define the EC2
lc = t.add_resource(LaunchConfiguration(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro",
    SecurityGroups=[Ref(SecurityGroup)],
    DependsOn="InstanceSecurityGroup"
))


# Define the Launch Configuration
LaunchConfig = t.add_resource(LaunchConfiguration(
    "LaunchConfiguration",
    ImageId=Ref(AmiId),
    SecurityGroups=[Ref(SecurityGroup)],
    InstanceType="t1.micro",
    DependsOn="InstanceSecurityGroup"
))

# Define the AutoScaling Group
AutoscalingGroup = t.add_resource(AutoScalingGroup(
    "AutoscalingGroup",
    DesiredCapacity=Ref(ScaleCapacity),
    Tags=[
        Tag("Environment", "test", True)
    ],
    LaunchConfigurationName=Ref(LaunchConfig),
    MinSize=1,
    MaxSize=Ref(ScaleCapacity),
    AvailabilityZones=['us-east-1a', 'us-east-1b'],
    HealthCheckType="EC2",
    UpdatePolicy=UpdatePolicy(
        AutoScalingReplacingUpdate=AutoScalingReplacingUpdate(
            WillReplace=True,
        ),
        AutoScalingRollingUpdate=AutoScalingRollingUpdate(
            PauseTime='PT5M',
            MinInstancesInService="1",
            MaxBatchSize='1',
            WaitOnResourceSignals=True
        )
    )
))

print(t.to_yaml())
