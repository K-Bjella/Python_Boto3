import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(CidrBlock='12.0.0.1/16')


print(vpc["Vpc"]["VpcId"])
