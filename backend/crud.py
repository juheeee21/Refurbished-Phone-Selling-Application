from sqlalchemy.orm import Session
from . import models, schemas

def create_phone(db: Session, phone: schemas.PhoneCreate):
    db_phone = models.Phone(
        brand=phone.brand,
        model=phone.model,
        condition=phone.condition,
        specs=phone.specs,
        stock=phone.stock,
        base_price=phone.base_price,
        tags=phone.tags or [],
        manual_price_overrides=phone.manual_price_overrides or {},
    )
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

def update_phone(db: Session, phone_id: int, phone: schemas.PhoneUpdate):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if not db_phone:
        return None
    for field, value in phone.dict().items():
        setattr(db_phone, field, value)
    db.commit()
    db.refresh(db_phone)
    return db_phone

def delete_phone(db: Session, phone_id: int):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if db_phone:
        db.delete(db_phone)
        db.commit()

def bulk_upload_phones(db: Session, df):
    added = []
    for _, row in df.iterrows():
        phone = models.Phone(
            brand=row['brand'],
            model=row['model'],
            condition=row['condition'],
            specs=eval(row['specs']),
            stock=int(row['stock']),
            base_price=float(row['base_price']),
            tags=row['tags'].split(",") if row['tags'] else [],
        )
        db.add(phone)
        added.append(phone)
    db.commit()
    return {"added": len(added)}

def get_phone(db: Session, phone_id: int):
    return db.query(models.Phone).filter(models.Phone.id == phone_id).first()

def create_platform_listing(db: Session, phone_id: int, platform, price, mapped_condition, status):
    listing = models.PlatformListing(
        phone_id=phone_id,
        platform=platform,
        price=price,
        mapped_condition=mapped_condition,
        listing_status=status,
    )
    db.add(listing)
    db.commit()

def search_phones(db: Session, search: str, condition: str, platform: str):
    query = db.query(models.Phone)
    if search:
        query = query.filter(
            (models.Phone.model.ilike(f"%{search}%")) | (models.Phone.brand.ilike(f"%{search}%"))
        )
    if condition:
        query = query.filter(models.Phone.condition == condition)
    if platform:
        # Filter phones with a successful listing on the platform
        phone_ids = (
            db.query(models.PlatformListing.phone_id)
            .filter(models.PlatformListing.platform == platform)
            .filter(models.PlatformListing.listing_status == "success")
            .distinct()
        )
        query = query.filter(models.Phone.id.in_(phone_ids))
    return query.all()

def manual_override_price(db: Session, phone_id: int, override: schemas.ManualOverride):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if not db_phone:
        return {"ok": False, "error": "Phone not found"}
    for plat in ["X", "Y", "Z"]:
        if getattr(override, plat, None):
            db_phone.manual_price_overrides[plat] = getattr(override, plat)
    db.commit()
    db.refresh(db_phone)
    return {"ok": True}
