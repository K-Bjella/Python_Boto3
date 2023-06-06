import boto3

vpc_id = "vpc-0127fc1ef863e0a0e"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
