from fastapi import Depends, Request

from .service import FilesService
from ..core.controller import Controller, Get
from ..decorators.validate_token import validate_token
from ..deps.auth_service_stub import AuthServiceStubDepend


@Controller('/')
class FilesController:
    file_service: FilesService = Depends(FilesService)

    @Get('/presigned-post')
    @validate_token
    def create_presigned_post(self, request: Request, auth_service_stub: AuthServiceStubDepend):
        return self.file_service.create_presigned_post()
