import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_types()

for instanceType in response ["InstanceTypes"]:
    print(instanceType["InstanceType"])
