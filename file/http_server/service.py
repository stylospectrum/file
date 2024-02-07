import uuid

from ..deps.s3 import S3ManagerDepend


class FilesService:
    def __init__(self, s3: S3ManagerDepend):
        self.s3 = s3

    def create_presigned_post(self):
        return self.s3.client.generate_presigned_post(self.s3.bucket_name, str(uuid.uuid4()))
