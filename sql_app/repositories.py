
from sqlalchemy.orm import Session
from . import models, schemas

class ItemRepo:

    @staticmethod
    async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(
            name=item.name,
            price=item.price,
            description=item.description,
            store_id=item.store_id
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def fetch_by_id(db: Session, _id):
        return db.query(models.Item).filter(models.Item.id == _id).first()

    @staticmethod
    def fetch_by_name(db: Session, name):
        return db.query(models.Item).filter(models.Item.name == name).first()

    @staticmethod
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Item).order_by(models.Item.id).offset(skip).limit(limit).all()

    @staticmethod
    async def delete(db: Session, item_id):
        db_item = db.query(models.Item).filter_by(id=item_id).first()
        db.delete(db_item)
        db.commit()

    @staticmethod
    async def update(db: Session, item_data):
        updated_item = db.merge(item_data)
        db.commit()
        return updated_item


class StoreRepo:

    @staticmethod
    async def create(db: Session, store: schemas.StoreCreate):
        db_store = models.Store(name=store.name)
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
        return db_store

    @staticmethod
    def fetch_by_id(db: Session, _id: int):
        return db.query(models.Store).filter(models.Store.id == _id).first()

    @staticmethod
    def fetch_by_name(db: Session, name: str):
        return db.query(models.Store).filter(models.Store.name == name).first()

    @staticmethod
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Store).order_by(models.Store.id).offset(skip).limit(limit).all()

    @staticmethod
    async def delete(db: Session, _id: int):
        db_store = db.query(models.Store).filter_by(id=_id).first()
        db.delete(db_store)
        db.commit()

    @staticmethod
    async def update(db: Session, store_data):
        updated_store = db.merge(store_data)
        db.commit()
        return updated_store
