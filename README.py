# Amazon_AWS
import boto3
from botocore.client import Config


s3 = boto3.resource(
    's3',
    aws_access_key_id='AKIAIWOJJA2TRONDEPWQ',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
)


data = open('test.py', 'rb')
s3.Bucket('samuelbucket1').put_object(Key='test/test.py', Body=data)
#Or
s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
s3.upload_file('test.sh', 'samuelbucket1', 'test.sh')
# s3.delete_bucket(Bucket='erewrewrewrrwerw3')
