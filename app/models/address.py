from flask import current_app, url_for, g
from app import db, geolocator
from sqlalchemy import event


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(255))
    street_number = db.Column(db.String(255))
    route = db.Column(db.String(255))
    apt_number = db.Column(db.String(255))
    locality = db.Column(db.String(255))
    administrative_area_level_1 = db.Column(db.String(2))
    postal_code = db.Column(db.String(255))
    county = db.Column(db.String(255))
    country = db.Column(db.String(255))
    latitude = db.Column(db.Numeric(precision=9, scale=6))
    longitude = db.Column(db.Numeric(precision=9, scale=6))

    def __init__(self, **kwargs):
        super(Address, self).__init__(**kwargs)

    def __repr__(self):
        return '{}, {}, {} {}'.format(self.street_address,
                                      self.locality,
                                      self.administrative_area_level_1,
                                      self.postal_code)

    def to_dict(self):
        data = {
            'id': self.id,
            'line_1': self.line_1,
            'line_2': self.line_2,
            'line_3': self.line_3,
            'line_4': self.line_4,
            'city': self.city,
            'state_code': self.state_code,
            'postal_code': self.postal_code,
            'county': self.county,
            'country': self.country
        }
        return data

    def from_dict(self, data):
        for field in data['line_1', 'line_2', 'line_3', 'line_4', 'city',
                          'state_code', 'postal_code', 'county', 'country']:
            if field in data:
                setattr(self, field, data[field])

    def geocode(self, **kwargs):
        line_1 = kwargs.get("street_address", self.street_address)
        city = kwargs.get("locality", self.locality)
        state_code = kwargs.get("administrative_area_level_1", self.administrative_area_level_1)
        postal_code = kwargs.get("postal_code", self.postal_code)
        self.latitude = None
        self.longitude = None
        try:
            location = geolocator.geocode('{} {} {} {}'.format(line_1,
                                                               city,
                                                               state_code,
                                                               postal_code))
            if location is not None:
                self.latitude = location.latitude
                self.longitude = location.longitude
        except:
            current_app.logger.error('Unable to geocode address')


def update_geocoding(mapper, connection, target):
    target.geocode()


event.listen(Address, 'before_insert', update_geocoding)
event.listen(Address, 'before_update', update_geocoding)
