import boto3
s3 = boto3.client('s3',
    aws_access_key_id= '',
    aws_secret_access_key= '')
s3.upload_fileobj(open(r"C:\Users\vitaliy\Desktop\project\DevOps-Base-Tools\task1\currency.txt", "rb"), "task2devops", "currency.txt")
