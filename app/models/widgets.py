from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .base import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict


# the definition of a thing
class Widget(Base):
    __tablename__ = 'widgets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    config = Column(MutableDict.as_mutable(JSONB))  # flexible json input
