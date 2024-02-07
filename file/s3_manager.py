import boto3

from .config.settings import settings


class S3Manager:
    def __init__(self):
        self.client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
            region_name=settings.REGION_NAME
        )

        self.bucket_name = settings.AWS_S3_BUCKET_NAME
