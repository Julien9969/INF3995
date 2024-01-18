from pydantic import BaseModel, Field
from datetime import datetime
from .classes.something_type import SomethingType


class SomethingBase(BaseModel):
    something: SomethingType
    value: float
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True