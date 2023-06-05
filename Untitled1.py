import boto3

s3 = boto3.client('s3')

s3.meta.client.download_file('kbjella-boto3-06022023', 'test_text_upload.txt', 'test_text_upload.txt')
