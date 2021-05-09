import boto3
s3 = boto3.client('s3',
    aws_access_key_id= 'AKIAU7WSZR4QVW5XWEY5',
    aws_secret_access_key= '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')
s3.upload_fileobj(open(r"C:\Users\vitaliy\Desktop\project\DevOps-Base-Tools\task1\currency.txt", "rb"), "task2devops", "currency.txt")
