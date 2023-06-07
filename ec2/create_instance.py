import boto3

ami_id = 'ami-0dd1bcc867dba6250'
key_pair_name = "key from boto3"
security_group_id = 'sg-092bb77c11645621b'

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id
    ]
    
 )

print(response)