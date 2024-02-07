from .service import FilesService
from .controller import FilesController

class FilesModule:
    controllers = [FilesController]
    services = [FilesService]