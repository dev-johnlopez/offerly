from flask import current_app, url_for, g
from app import db, geolocator
from sqlalchemy import event
from app.models.address import Address


class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer, primary_key=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', uselist=False)
    sq_foot = db.Column(db.Integer)
    year_built = db.Column(db.Integer)
    stories_count = db.Column(db.Integer)
    basement_type = db.Column(db.String(255))
    addition_type = db.Column(db.String(255))
    bedroom_count = db.Column(db.Integer)
    full_bath_count = db.Column(db.Integer)
    half_bath_count = db.Column(db.Integer)
    parking_type = db.Column(db.String(255))
    countertops = db.Column(db.String(255))
    appliances = db.Column(db.String(255))
    double_oven_ind = db.Column(db.Boolean)
    walk_in_pantry_ind = db.Column(db.Boolean)
    separate_cooktop_ind = db.Column(db.Boolean)
    built_in_oven_ind = db.Column(db.Boolean)
    built_in_microwave_ind = db.Column(db.Boolean)
    kitchen_flooring = db.Column(db.String(255))
    main_flooring = db.Column(db.String(255))
    bathroom_flooring_tile_ind = db.Column(db.Boolean)
    bathroom_flooring_vinyl_ind = db.Column(db.Boolean)
    bathroom_flooring_laminate_ind = db.Column(db.Boolean)
    bathroom_flooring_hardwood_ind = db.Column(db.Boolean)
    bathroom_flooring_travertine_ind = db.Column(db.Boolean)
    bathroom_flooring_saltillo_tile_ind = db.Column(db.Boolean)
    bathroom_flooring_carpet_ind = db.Column(db.Boolean)
    bathroom_flooring_woodplank_tile_ind = db.Column(db.Boolean)
    bathroom_flooring_concrete_ind = db.Column(db.Boolean)
    bathroom_flooring_other_ind = db.Column(db.Boolean)
    bedroom_flooring_tile_ind = db.Column(db.Boolean)
    bedroom_flooring_vinyl_ind = db.Column(db.Boolean)
    bedroom_flooring_laminate_ind = db.Column(db.Boolean)
    bedroom_flooring_hardwood_ind = db.Column(db.Boolean)
    bedroom_flooring_travertine_ind = db.Column(db.Boolean)
    bedroom_flooring_saltillo_tile_ind = db.Column(db.Boolean)
    bedroom_flooring_carpet_ind = db.Column(db.Boolean)
    bedroom_flooring_woodplank_tile_ind = db.Column(db.Boolean)
    bedroom_flooring_concrete_ind = db.Column(db.Boolean)
    bedroom_flooring_other_ind = db.Column(db.Boolean)
    landscaping = db.Column(db.String(255))
    pool = db.Column(db.Boolean)
    hottub = db.Column(db.Boolean)
    gated_community_ind = db.Column(db.Boolean)
    hoa_ind = db.Column(db.Boolean)
    age_restricted_ind = db.Column(db.Boolean)
    solar_panels_ind = db.Column(db.Boolean)
    septic_system_ind = db.Column(db.Boolean)
    well_water_ind = db.Column(db.Boolean)
    poor_location_ind = db.Column(db.Boolean)
    sinkholes_ind = db.Column(db.Boolean)
    foundation_issues = db.Column(db.Boolean)
    additional_info = db.Column(db.String(1500))
    submitter_type = db.Column(db.String(255))
    listed_ind = db.Column(db.Boolean)
    submitter_first_name = db.Column(db.String(255))
    submitter_last_name = db.Column(db.String(255))
    submitter_phone = db.Column(db.String(255))
    submitter_email = db.Column(db.String(255))
