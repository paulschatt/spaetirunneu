from ..models import spaetirun as models
from ..schemas import spaetirun as schemas
from .base import CRUDRepository

spaetirun_repo = CRUDRepository[models.Spaetirun, schemas.SpaetirunCreate, schemas.SpaetirunUpdate](models.Spaetirun)