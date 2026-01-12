from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Generic, TypeVar, List
from pydantic import BaseModel
from ..database import get_db

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseCRUDRouter(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    router = APIRouter()
    @router.get("/", response_model=List[ModelType])
    def get_all(self, db: Session = Depends(get_db)):
        return self.get_all(db)

    @router.get("/{item_id}", response_model=ModelType)
    def get(self, item_id: int, db: Session = Depends(get_db)):
        db_item = self.get(db, item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item

    @router.post("/", response_model=ModelType, status_code=201)
    def create(self, item: CreateSchemaType, db: Session = Depends(get_db)):
        return self.create(db, item)

    @router.put("/{item_id}", response_model=ModelType)
    def update(self, item_id: int, item: UpdateSchemaType, db: Session = Depends(get_db)):
        db_item = self.update(db, item_id, item)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item

    @router.delete("/{item_id}", status_code=204)
    def delete(self, item_id: int, db: Session = Depends(get_db)):
        success = self.delete(db, item_id)
        if not success:
            raise HTTPException(status_code=404, detail="Item not found")
