
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SpaetirunBase(BaseModel):
    name: str

class SpaetirunCreate(SpaetirunBase):
    pass  # same as base

class SpaetirunUpdate(SpaetirunBase):
    pass # same as base

class Spaetirun(SpaetirunBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # maps from ORM objects