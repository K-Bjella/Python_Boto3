import boto3

route_table_id = "rtb-099e7149754e53457"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)

