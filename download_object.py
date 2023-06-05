import boto3

s3 = boto3.client('s3')
key = 'test_text_upload.txt'
filename = 'test_text_upload.txt'

def download_single_object(client, bucket, key, Filename)
    client.download_file(bucket, key, filename)

