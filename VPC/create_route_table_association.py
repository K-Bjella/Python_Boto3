import boto3

route_table_id = 'rtb-099e7149754e53457'
subnet_id = 'subnet-02332ef9a471e6f02'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])
