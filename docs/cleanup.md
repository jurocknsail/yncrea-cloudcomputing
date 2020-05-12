# Cleanup Resources

All the EC2, ECS, EKS etc ... ressources that your deployed are expensive !  
Delete : 
 
-  The CloudFormation stacks for the EC2 and ECS : from `aws cli` or the web interface
-  The EKS cluster : `eksctl delete cluster <your_cluster_name>`