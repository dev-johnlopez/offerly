from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FormField, BooleanField, \
                    TextAreaField, SelectField, FieldList, HiddenField, \
                    RadioField
from wtforms.validators import DataRequired, Optional
from app.models.address import Address


class LandingAddressForm(FlaskForm):
    street_address = StringField('Street Address', validators=[Optional()])
    street_number = StringField('Street Number', validators=[Optional()])
    route = StringField('Route', validators=[Optional()])
    apt_number = StringField('Apt / Unit #', validators=[Optional()])
    locality = StringField('City', validators=[Optional()])
    administrative_area_level_1 = SelectField('State', choices=[
        ('', ''),
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CT', 'Connecticut'),
        ('DC', 'Washington DC'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming')
    ], validators=[Optional()])
    postal_code = StringField('ZIP Code', validators=[Optional()])
    country = StringField('Country', validators=[Optional()])


class AddressForm(FlaskForm):
    street_address = StringField('Street Address', validators=[DataRequired()])
    street_number = StringField('Street Number', validators=[Optional()])
    route = StringField('Route', validators=[Optional()])
    apt_number = StringField('Apt / Unit #', validators=[Optional()])
    locality = StringField('City', validators=[Optional()])
    administrative_area_level_1 = SelectField('State', choices=[
        ('', ''),
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CT', 'Connecticut'),
        ('DC', 'Washington DC'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming')
    ], validators=[DataRequired()])
    postal_code = StringField('ZIP Code', validators=[DataRequired()])
    country = StringField('Country', validators=[Optional()])


class PropertyForm(FlaskForm):
    address = FormField(AddressForm, default=lambda: Address())
    sq_foot = IntegerField('What is the square footage of the home?',
                           description='Do not include basement, \
                                        non-permitted additions, or \
                                        non-heated square footage.',
                           validators=[Optional()])
    year_built = IntegerField('What year was the home built?',
                              description='(For example, 2001)',
                              validators=[Optional()])
    stories_count = RadioField('How many stories does the home have?',
                               description="Don't include a basement... \
                                            We will git to that later.",
                               choices=[
                                    ('1', 'One story'),
                                    ('2', 'Two story'),
                                    ('3', 'Three story')],
                               validators=[Optional()])
    basement_type = RadioField('Does the home have a basement?',
                               description='A basement is a level that is \
                                            either completely or partially \
                                            below the ground floor. Finished \
                                            means that the space is sutable \
                                            for living, with fully finished \
                                            walls, flooring, as well as air \
                                            conditioning and heating.',
                               choices=[
                                    ('none', 'No Basement'),
                                    ('unfinished', 'Unfinished Basement'),
                                    ('partial', 'Partially Finished Basement'),
                                    ('finished', 'Finished Basement')
                               ],
                               validators=[Optional()])
    addition_type = RadioField('Have you or the previous owners made \
                                additions to the structure of the home?',
                               description='Additions include garages that \
                                            may have been converted, \
                                            sunrooms, bonus rooms, or any \
                                            other living area extensions.',
                               choices=[
                                    ('none', 'No additions'),
                                    ('additions-no-permits',
                                        'Additions without permits'),
                                    ('garage-no-permit',
                                        'Garage conversion without permits'),
                                    ('porch-no-permit',
                                        'Porch conversion without permits'),
                                    ('additions-with-permits',
                                        'Additions with permits'),
                                    ('garage-with-pemrit',
                                        'Garage conversion with permits'),
                                    ('porch-with-permit',
                                        'Porch conversion with permits')
                               ],
                               validators=[Optional()])
    bedroom_count = RadioField('How many bedrooms does the home have?',
                               description='A room counts as a bedroom if \
                                            it has a closet, door, \
                                            and window.',
                               choices=[
                                    ('0', 'Studio'),
                                    ('1', '1 Bed'),
                                    ('2', '2 Beds'),
                                    ('3', '3 Beds'),
                                    ('4', '4 Beds'),
                                    ('5', '5+ Beds')
                               ],
                               validators=[Optional()])
    full_bath_count = RadioField('How many full bathrooms does the home have?',
                                 description='A room counts as a full \
                                              bathroom if it includes a \
                                              toilet, sink and \
                                              bathtub/shower.',
                                 choices=[
                                    ('1', '1'),
                                    ('2', '2'),
                                    ('3', '3'),
                                    ('4', '4'),
                                    ('5', '5+')
                                 ],
                                 validators=[Optional()])
    half_bath_count = RadioField('How many half bathrooms does the home have?',
                                 description='A room counts as a half \
                                              bathroom if it includes a \
                                              toilet and sink but no \
                                              bathtub/shower.',
                                 choices=[
                                    ('1', '1'),
                                    ('2', '2'),
                                    ('3', '3'),
                                    ('4', '4'),
                                    ('5', '5+')
                                 ],
                                 validators=[Optional()])
    parking_type = RadioField('What kind of parking or garage does the \
                               home have?',
                              choices=[
                                ('single', '1-Car Garage'),
                                ('double', '2-Car Garage'),
                                ('triple', '3-Car Garage'),
                                ('quad', '4-Car Garage'),
                                ('1carport', '1 Carport'),
                                ('2carport', '2 Carport'),
                                ('outside', 'Outside'),
                                ('street', 'Street'),
                                ('other', 'Other')
                              ],
                              validators=[Optional()])
    countertops = RadioField('What kind of countertops are in the kitchen?',
                             description='Select the option that most closely \
                                          describes your counter tops.',
                             choices=[
                                ('granite-slab', 'Granite Slab'),
                                ('granite-tile', 'Granite Tile'),
                                ('quartz', 'Quartz'),
                                ('corian', 'Corian'),
                                ('laminate', 'Laminate'),
                                ('tile', 'Tile')
                             ],
                             validators=[Optional()])
    appliances = RadioField('What kind of appliances does the kitchen have?',
                            choices=[
                                ('stainless', 'Stainless Steel'),
                                ('black', 'Black'),
                                ('white', 'White'),
                                ('mixed', 'Mixed')
                            ],
                            validators=[Optional()])
    double_oven_ind = BooleanField('Double oven')
    walk_in_pantry_ind = BooleanField('Walk-in pantry')
    separate_cooktop_ind = BooleanField('Separate cooktop')
    built_in_oven_ind = BooleanField('Built-in wall oven')
    built_in_microwave_ind = BooleanField('Built-in microwave')
    kitchen_flooring = RadioField('What type of flooring is used in \
                                   the kitchen?',
                                  description='Select the option that most \
                                               closely matches the flooring.',
                                  choices=[
                                    ('tile', 'Tile'),
                                    ('vinyl', 'Vinyl'),
                                    ('laminate', 'Laminate'),
                                    ('hardwood', 'Hardwood'),
                                    ('travertine', 'Travertine'),
                                    ('saltillo-tile', 'Saltillo Tile'),
                                    ('carpet', 'Carpet'),
                                    ('woodplank-tile', 'Woodplank Tile'),
                                    ('concrete', 'Concrete'),
                                    ('other', 'other')
                                  ],
                                  validators=[Optional()])
    main_flooring = RadioField('What type of flooring is used in the main \
                                living areas?',
                               description='Select the option that most \
                                            closely matches the flooring.',
                               choices=[
                                    ('tile', 'Tile'),
                                    ('vinyl', 'Vinyl'),
                                    ('laminate', 'Laminate'),
                                    ('hardwood', 'Hardwood'),
                                    ('travertine', 'Travertine'),
                                    ('saltillo-tile', 'Saltillo Tile'),
                                    ('carpet', 'Carpet'),
                                    ('woodplank-tile', 'Woodplank Tile'),
                                    ('concrete', 'Concrete'),
                                    ('other', 'other')
                               ],
                               validators=[Optional()])
    bathroom_flooring_tile_ind = BooleanField('Tile')
    bathroom_flooring_vinyl_ind = BooleanField('Vinyl')
    bathroom_flooring_laminate_ind = BooleanField('Laminate')
    bathroom_flooring_hardwood_ind = BooleanField('Hardwood')
    bathroom_flooring_travertine_ind = BooleanField('Travertine')
    bathroom_flooring_saltillo_tile_ind = BooleanField('Saltillo Tile')
    bathroom_flooring_carpet_ind = BooleanField('Carpet')
    bathroom_flooring_woodplank_tile_ind = BooleanField('Woodplank Tile')
    bathroom_flooring_concrete_ind = BooleanField('Concrete')
    bathroom_flooring_other_ind = BooleanField('Other')
    bedroom_flooring_tile_ind = BooleanField('Tile')
    bedroom_flooring_vinyl_ind = BooleanField('Vinyl')
    bedroom_flooring_laminate_ind = BooleanField('Laminate')
    bedroom_flooring_hardwood_ind = BooleanField('Hardwood')
    bedroom_flooring_travertine_ind = BooleanField('Travertine')
    bedroom_flooring_saltillo_tile_ind = BooleanField('Saltillo Tile')
    bedroom_flooring_carpet_ind = BooleanField('Carpet')
    bedroom_flooring_woodplank_tile_ind = BooleanField('Woodplank Tile')
    bedroom_flooring_concrete_ind = BooleanField('concrete')
    bedroom_flooring_other_ind = BooleanField('other')
    landscaping = RadioField('Does the home have landscaping?',
                             choices=[
                                ('none', 'None'),
                                ('both', 'Both front and back yard'),
                                ('front', 'Front yard only'),
                                ('back', 'Back yard only')
                             ],
                             validators=[Optional()])
    pool = RadioField('Does the home have an in-ground pool?',
                      choices=[
                         (True, 'Yes'),
                         (False, 'No')
                      ], coerce=lambda x: x == 'True',
                      validators=[Optional()])
    hottub = RadioField('Does the home have an in-ground spa / hot tub?',
                        choices=[
                           (True, 'Yes'),
                           (False, 'No')
                        ], coerce=lambda x: x == 'True',
                        validators=[Optional()])
    gated_community_ind = BooleanField('Gated Community')
    hoa_ind = BooleanField('Homeowners Association')
    age_restricted_ind = BooleanField('Age Restricted')
    solar_panels_ind = BooleanField('Solar Panels')
    septic_system_ind = BooleanField('Septic System')
    well_water_ind = BooleanField('Well Water')
    poor_location_ind = BooleanField('The property backs to a busy road, \
                                      commercial buildings, or power lines')
    sinkholes_ind = RadioField('Are you aware of sinkholes on the property?',
                               choices=[
                                  (True, 'Yes'),
                                  (False, 'No')
                               ], coerce=lambda x: x == 'True',
                               validators=[Optional()])
    foundation_issues = RadioField('Are there foundation issues?',
                                   choices=[
                                    (True, 'Yes'),
                                    (False, 'No')
                                   ], coerce=lambda x: x == 'True',
                                   validators=[Optional()])
    additional_info = TextAreaField('Is there anything else you would like to \
                                     tell us?',
                                    description='This field is optional but \
                                                it gives you teh opportunity \
                                                to tell us what is special \
                                                about the home. \
                                                (Max 1500 characters)')
    submitter_type = RadioField('What is your relationship to this home?',
                                choices=[
                                    ('owner', 'Owner'),
                                    ('agent', 'Real Estate Agent'),
                                    ('other', 'Other')
                                ],
                                validators=[Optional()])
    listed_ind = RadioField('Is this home listed on the MLS?',
                            choices=[
                               (True, 'Yes'),
                               (False, 'No')
                            ], coerce=lambda x: x == 'True',
                            validators=[Optional()])
    submitter_first_name = StringField('First Name',
                                       validators=[DataRequired()])
    submitter_last_name = StringField('Last Name',
                                      validators=[DataRequired()])
    submitter_phone = StringField('Phone',
                                  validators=[DataRequired()])
    submitter_email = StringField('Email',
                                  validators=[DataRequired()])
