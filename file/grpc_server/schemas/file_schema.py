import uuid
    
from datetime import datetime
from sqlmodel import SQLModel, Field


class File(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True)
    owner_id: str
    type: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False)
