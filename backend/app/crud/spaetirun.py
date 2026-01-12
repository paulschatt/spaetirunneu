from .. import models, schemas

spaetirun_repo = CRUDRepository[models.Spaetirun, schemas.SpaetirunCreate, schemas.SpaetirunUpdate](models.Spaetirun)