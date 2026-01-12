from base import BaseCRUDRouter
from .. import crud, schemas

class SpaetirunRouter(BaseCRUDRouter[schemas., schemas.TeamCreate, schemas.TeamUpdate]):
    router = APIRouter(prefix="/spaetirun")

    def get_all(self, db):
        return crud.spaetirun.get_all(db)

    def get(self, db, item_id):
        return crud.team.get(db, item_id)

    def create(self, db, item):
        return crud.team.create(db, item)

    def update(self, db, item_id, item):
        return crud.team.update(db, item_id, item)

    def delete(self, db, item_id):
        return crud.team.delete(db, item_id)