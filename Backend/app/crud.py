from fastapi import HTTPException
from sqlalchemy.orm import Session
from .classes.something_type import SomethingType

from . import models

def get_something(db: Session, id: int, something_type: SomethingType):
    db_something = db.query(models.Something).filter_by(id=id, something_type=something_type).first()
    if db_something == None:
        raise HTTPException(status_code=404, detail="Something not found")
    return db_something