from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import pandas as pd
from typing import List, Optional
from . import models, schemas, crud, utils, auth, database

app = FastAPI(title="Refurbished Phone Selling App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

@app.post("/login", response_model=schemas.UserToken)
def login(user: schemas.UserLogin):
    return auth.mock_login(user)

@app.post("/phones/", response_model=schemas.Phone)
def add_phone(
    phone: schemas.PhoneCreate,
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user)
):
    return crud.create_phone(db, phone)

@app.put("/phones/{phone_id}", response_model=schemas.Phone)
def update_phone(
    phone_id: int,
    phone: schemas.PhoneUpdate,
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user)
):
    return crud.update_phone(db, phone_id, phone)

@app.delete("/phones/{phone_id}")
def delete_phone(
    phone_id: int,
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user)
):
    crud.delete_phone(db, phone_id)
    return {"ok": True}

@app.post("/phones/bulk_upload")
def bulk_upload(
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user),
):
    df = pd.read_csv(file.file)
    return crud.bulk_upload_phones(db, df)

@app.get("/phones/", response_model=List[schemas.Phone])
def list_phones(
    search: Optional[str] = "",
    condition: Optional[str] = "",
    platform: Optional[str] = "",
    db: Session = Depends(database.get_db)
):
    return crud.search_phones(db, search, condition, platform)

@app.post("/phones/{phone_id}/list/{platform}", response_model=schemas.PlatformListingResult)
def list_on_platform(
    phone_id: int,
    platform: str,
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user)
):
    phone = crud.get_phone(db, phone_id)
    if not phone:
        raise HTTPException(status_code=404, detail="Phone not found")
    if phone.stock <= 0 or "out of stock" in phone.tags:
        return schemas.PlatformListingResult(success=False, error="Out of stock")
    fee_info = utils.get_platform_fee(platform)
    price, err = utils.calc_platform_price(phone.base_price, platform, fee_info, phone.manual_price_overrides)
    if err:
        return schemas.PlatformListingResult(success=False, error=err)
    mapped_condition = utils.map_condition(phone.condition, platform)
    if not mapped_condition:
        return schemas.PlatformListingResult(success=False, error="Condition not supported")
    # Simulate high-fee rejection logic
    min_profit = 15  # e.g., don't list if profit < $15
    profit = price - phone.base_price
    if profit < min_profit:
        return schemas.PlatformListingResult(success=False, error="Fee too high, unprofitable")
    # Register listing as simulated
    crud.create_platform_listing(db, phone_id, platform, price, mapped_condition, "success")
    return schemas.PlatformListingResult(success=True, platform=platform, price=price, mapped_condition=mapped_condition)

@app.post("/phones/{phone_id}/manual_override")
def manual_override(
    phone_id: int,
    override: schemas.ManualOverride,
    db: Session = Depends(database.get_db),
    user=Depends(auth.get_current_user)
):
    return crud.manual_override_price(db, phone_id, override)
