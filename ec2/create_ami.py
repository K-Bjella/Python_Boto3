import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-06f029504c8929631',
    Name='Go To Ami',
)

print(response["ImageId"])