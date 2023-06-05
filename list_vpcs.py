import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()

for vpc in response["Vpcs"]:
    print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])
    
for vpc in response["Vpcs"]:
    if "Tags" in vpc:
        for tag in vpc["Tags"]:
            if "Name" == tag['Key']:
                print(tag["Value"])