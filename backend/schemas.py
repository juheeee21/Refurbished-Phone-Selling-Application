from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserToken(BaseModel):
    token: str

class Specs(BaseModel):
    storage: Optional[str]
    color: Optional[str]

class ManualOverride(BaseModel):
    X: Optional[float]
    Y: Optional[float]
    Z: Optional[float]

class PhoneBase(BaseModel):
    brand: str
    model: str
    condition: str
    specs: Dict[str, Any]
    stock: int
    base_price: float
    tags: Optional[List[str]] = []
    manual_price_overrides: Optional[Dict[str, float]] = {}

class PhoneCreate(PhoneBase):
    pass

class PhoneUpdate(PhoneBase):
    pass

class Phone(PhoneBase):
    id: int
    class Config:
        orm_mode = True

class PlatformListingResult(BaseModel):
    success: bool
    platform: Optional[str] = None
    price: Optional[float] = None
    mapped_condition: Optional[str] = None
    error: Optional[str] = None
