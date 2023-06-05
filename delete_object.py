import boto3

def delete_object(client, bucket, key):
    response = s3.delete_object(
    Bucket=bucket,
    Key=key,
)

bucket = "kbjella-boto3-06022023"
key = "test_text.txt"

s3 = boto3.client('s3')

keys = ["test_text_string.txt", "test_text_upload.txt"]

for key in keys:
    delete_object(s3, bucket, key)