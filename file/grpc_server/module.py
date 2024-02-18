import grpc
import logging

from concurrent import futures

from .service import FileServicer
from ..proto.file import file_pb2_grpc
from ..config.settings import settings
from ..s3_manager import S3Manager


def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    file_pb2_grpc.add_FileServiceServicer_to_server(
        FileServicer(s3=S3Manager()), server)
    server.add_insecure_port(f"[::]:{settings.SERVICE_URL}")
    server.start()
    
    logging.basicConfig(level=logging.INFO)
    logging.info("gRPC server running...")

    return server
