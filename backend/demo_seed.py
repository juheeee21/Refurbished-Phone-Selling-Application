from . import database, crud, schemas

def seed():
    db = next(database.get_db())
    # Add demo phones
    phones = [
        schemas.PhoneCreate(
            brand="Apple", model="iPhone X", condition="Good",
            specs={"storage": "64GB", "color": "Black"}, stock=5,
            base_price=250, tags=[], manual_price_overrides={}
        ),
        schemas.PhoneCreate(
            brand="Samsung", model="Galaxy S10", condition="New",
            specs={"storage": "128GB", "color": "White"}, stock=3,
            base_price=320, tags=[], manual_price_overrides={}
        ),
        schemas.PhoneCreate(
            brand="Nokia", model="3310", condition="Scrap",
            specs={"storage": "16MB", "color": "Blue"}, stock=0,
            base_price=20, tags=["out of stock"], manual_price_overrides={}
        ),
    ]
    for p in phones:
        crud.create_phone(db, p)
    db.close()

if __name__ == "__main__":
    seed()
