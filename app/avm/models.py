# from datetime import datetime
from app import db


class AVM(db.Model):
    __tablename__ = 'AVM'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(125), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    zipcode = db.Column(db.String(125))
    city = db.Column(db.String(125))
    year_of_construction = db.Column(db.Integer)
    year_of_renovation = db.Column(db.Integer)
    total_price = db.Column(db.Integer, nullable=False)
    total_area = db.Column(db.Integer, nullable=False)
    price_m2 = db.Column(db.Integer, nullable=False)
    has_elevator = db.Column(db.Boolean)
    valuation_date = db.Column(db.Date)
    created_on = db.Column(
        db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())

    def serialize(self):
        return {
            "id": self.id,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "zipcode": self.zipcode,
            "city": self.city,
            "year_of_construction": self.year_of_construction,
            "year_of_renovation": self.year_of_renovation,
            "total_price": self.total_price,
            "total_area": self.total_area,
            "price_m2": self.price_m2,
            "has_elevator": self.has_elevator,
            "valuation_date": self.valuation_date,
            "created_on": self.created_on,
            "updated_on": self.updated_on,
        }
