from marshmallow import Schema, fields


class AVMSchema(Schema):

    id = fields.Int()
    address = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    zipcode = fields.Str()
    city = fields.Str()
    year_of_construction = fields.Int()
    year_of_renovation = fields.Int()
    total_price = fields.Int(required=True)
    total_area = fields.Int(required=True)
    price_m2 = fields.Int(required=True)
    has_elevator = fields.Bool()
    valuation_date = fields.Date()
