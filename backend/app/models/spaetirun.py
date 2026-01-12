from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from ..db.database import Base

class Spaetirun(Base):
    __tablename__ = "spaetirun"

    id = Column(UUID, primary_key=True, index=False)
    name = Column(String, index=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
