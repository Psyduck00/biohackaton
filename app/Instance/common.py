from .base import Base
from .sqlalchemy_guid import GUID
from sqlalchemy import Column, DateTime, Integer
import uuid
from datetime import datetime
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import func

class Common(Base):
    __abstract__ = True

    unique_identifier = Column(GUID, default=uuid.uuid4)