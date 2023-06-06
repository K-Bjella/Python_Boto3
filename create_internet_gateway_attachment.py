import boto3

internet_gateway_id = 'igw-021ef4ed2d015b619'
vpc_id = 'vpc-0127fc1ef863e0a0e'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

