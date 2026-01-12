from .base import BaseCRUDRouter
from fastapi import APIRouter
from ..schemas import spaetirun as schemas
from ..crud import spaetirun as crud

class SpaetirunRouter(BaseCRUDRouter[schemas.SpaetirunBase, schemas.SpaetirunCreate, schemas.SpaetirunUpdate]):
    router = APIRouter(prefix="/spaetirun")

    def get_all(self, db):
        return crud.get_all(db)

    def get(self, item_id, db):
        return crud.get(db, item_id)

    def create(self, item, db):
        return crud.create(db, item)

    def update(self, db, item_id, item):
        return crud.update(db, item_id, item)

    def delete(self, db, item_id):
        return crud.delete(db, item_id)