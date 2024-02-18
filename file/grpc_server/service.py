from sqlmodel import Session, select

from ..proto.file import file_pb2_grpc, file_pb2
from .schemas.file_schema import File
from ..postgres.engine import engine
from ..s3_manager import S3Manager


class FileServicer(file_pb2_grpc.FileServiceServicer):
    def __init__(self, s3: S3Manager):
        self.s3 = s3

    def CreateFile(self, request, context):
        with Session(engine) as session:
            file = session.exec(select(File).where(
                File.owner_id == request.owner_id)).first()

            if file is None:
                new_file = File(id=request.id, owner_id=request.owner_id,
                                type=request.type)
                session.add(new_file)
                session.commit()
            else:
                if str(file.id) == request.id:
                    return file_pb2.CreateFileResponse(success=True)


                self.s3.client.delete_object(Bucket=self.s3.bucket_name,
                                             Key=str(file.id),)

                if request.id:
                    file.id = request.id
                    session.add(file)
                    session.commit()
                else:
                    session.delete(file)
                    session.commit()

        return file_pb2.CreateFileResponse(success=True)

    def GetFile(self, request, context):
        url = ''
        with Session(engine) as session:
            file = session.exec(select(File).where(
                File.owner_id == request.owner_id)).first()

            if file:
                url = self.s3.client.generate_presigned_url('get_object',
                                                            Params={'Bucket': self.s3.bucket_name,
                                                                    'Key': str(file.id)})

        return file_pb2.GetFileResponse(url=url)

    def DeleteFile(self, request, context):
        with Session(engine) as session:
            file = session.exec(select(File).where(
                File.owner_id == request.owner_id)).first()

            if file:
                self.s3.client.delete_object(Bucket=self.s3.bucket_name,
                                             Key=str(file.id),)
                session.delete(file)
                session.commit()

        return file_pb2.DeleteFileResponse(success=True)
