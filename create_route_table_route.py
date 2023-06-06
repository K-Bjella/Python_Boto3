import boto3

route_table_id = 'rtb-099e7149754e53457'
internet_gateway_id = 'igw-021ef4ed2d015b619'


ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
