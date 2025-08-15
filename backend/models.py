from sqlalchemy import Column, Integer, String, Float, JSON, PickleType, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    condition = Column(String, index=True)
    specs = Column(JSON)
    stock = Column(Integer, default=0)
    base_price = Column(Float)
    tags = Column(PickleType)  # List[str]
    manual_price_overrides = Column(JSON, default={})

    listings = relationship("PlatformListing", back_populates="phone", cascade="all, delete-orphan")

class PlatformListing(Base):
    __tablename__ = "platformlistings"
    id = Column(Integer, primary_key=True, index=True)
    phone_id = Column(Integer, ForeignKey('phones.id'))
    platform = Column(String)
    price = Column(Float)
    mapped_condition = Column(String)
    listing_status = Column(String)

    phone = relationship("Phone", back_populates="listings")
