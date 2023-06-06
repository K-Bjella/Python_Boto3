import boto3

subnet_id = "subnet-02332ef9a471e6f02"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

