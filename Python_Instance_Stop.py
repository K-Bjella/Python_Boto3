import boto3  # Importing the boto3 library for interacting with AWS services

key_pair_name = "Python_project"  # Name of the key pair for SSH access
security_group_id = "sg-0358f92607288bb63"  # ID of the security group to associate with the instance
 
ec2 = boto3.client('ec2')

def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    response = client.run_instances(
            ImageId=ami_id,  # Specify the AMI ID
            InstanceType='t2.micro',  # Specify the instance type
            KeyName=key_pair_name,  # Specify the key pair name
            MaxCount=3,  # Specify the maximum number of instances to launch
            MinCount=3,  # Specify the minimum number of instances to launch
            SecurityGroupIds=[security_group_id],# Specify the security group ID
            TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Environment',
                        'Value': 'Dev'
                    },
                ]
            },
        ]
    )

    print(response["Instances"][0]["InstanceId"])  # Print the ID of the launched instance
    
ec2 = boto3.client('ec2')  # Creating an EC2 client object
create_instance(ec2, ami_id, security_group_id, key_pair_name)

###import boto3
# Create an EC2 client
###ec2 = boto3.client('ec2')
# Retrieve all running instances with the Environment: Dev tag
###response = ec2.describe_instances(Filters=[
   ### {'Name': 'instance-state-name', 'Values': ['running']},
    ###{'Name': 'tag:Environment', 'Values': ['Dev']}
###])
###instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

 

# Stop all running instances with the Environment: Dev tag
###if instances:
   ### ec2.stop_instances(InstanceIds=instances)
    ###print("Stopped the following Dev instances:")
    ###for instance in instances:
       ### print(instance)
###else:
   ### print("No running Dev instances found.")