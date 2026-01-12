from sqlalchemy.orm import Session
from typing import Generic, TypeVar, Type, List, Optional
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, item_id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == item_id).first()

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, item: CreateSchemaType) -> ModelType:
        db_item = self.model(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update(self, db: Session, item_id: int, item: UpdateSchemaType) -> Optional[ModelType]:
        db_item = self.get(db, item_id)
        if db_item:
            update_data = item.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_item, key, value)
            db.commit()
            db.refresh(db_item)
        return db_item

    def delete(self, db: Session, item_id: int) -> bool:
        db_item = self.get(db, item_id)
        if db_item:
            db.delete(db_item)
            db.commit()
            return True
        return False