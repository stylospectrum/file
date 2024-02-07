
from typing import Annotated
from fastapi import Depends

from ..s3_manager import S3Manager


S3ManagerDepend = Annotated[S3Manager, Depends(S3Manager)]
