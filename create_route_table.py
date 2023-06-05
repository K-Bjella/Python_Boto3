import boto3

vpc_id = "vpc-0127fc1ef863e0a0e"

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])#fix
