from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import (
    StringField, 
    SelectField, 
    SelectMultipleField, 
    DateTimeField, 
    BooleanField
)
from wtforms.validators import (
    DataRequired, 
    AnyOf,
    Optional, 
    URL, 
    ValidationError,
    Regexp,
    Length
    )
from flask_wtf.csrf import CSRFProtect
import os
import re
from datetime import timedelta

# length check -> re-use
# def length_check_120_char(form, field):
#     if len(field.data) > 120:
#         raise ValidationError('Field must be less than 120 characters.')

def is_valid_phone(number):
    """Validate phone number like:
    1234567890 - no space
    123.456.7890 - dot separator
    123-456-7890 - dash separator
    123 456 7890 - space separator

    Patterns:
    000 = [0-9]{3}
    0000 = [0-9]{4}
    -.  = ?[-. ]

    Note: (? = optional) - Learn more: https://regex101.com/"""

    regex = re.compile('^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$')
    return regex.match(number)

class ShowForm(Form):
    artist_id = StringField(
        'artist_id', validators=[DataRequired('Must be filled.')]
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired('Must be filled.')]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today() + timedelta(days = 7)
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired('Must be filled.'), Length(max=120, message='Field must be less than 120 characters.')]
    )
    city = StringField(
        'city', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')]
    )
    state = SelectField(
        'state', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')]
    )
    phone = StringField(
        'phone', validators=[Length(max=120,  message='Field must be less than 120 characters.')]
    )
    image_link = StringField(
        'image_link', validators=[Length(max=500,  message='Field must be less than 500 characters.')]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'), 
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    facebook_link = StringField(
        'facebook_link', validators=[Optional(), URL(), Length(max=500,  message='Field must be less than 120 characters.')]
    )
    website_link = StringField(
        'website_link', validators=[Optional(), URL(), Length(max=500,  message='Field must be less than 500 characters.')]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description', validators=[Length(max=500,  message='Field must be less than 500 characters.')]
    )

    def validate(self):
        """Custom validate method"""
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Invalid phone number.')
            return False
        # if pass validation
        return True

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired('Must be filled.'), Length(max=120, message='Field must be less than 120 characters.')]
    )
    city = StringField(
        'city', validators=[DataRequired('Must be filled.'), Length(max=120, message='Field must be less than 120 characters.')]
    )
    state = SelectField(
        'state', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[Length(max=120,  message='Field must be less than 120 characters.')]
    )
    image_link = StringField(
        'image_link', validators=[Optional(), URL(), Length(max=120,  message='Field must be less than 120 characters.')]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired('Must be filled.'), Length(max=120,  message='Field must be less than 120 characters.')],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[Optional(), URL(), Length(max=120,  message='Field must be less than 120 characters.')]
     )

    website_link = StringField(
        'website_link', validators=[Length(max=500,  message='Field must be less than 500 characters.')]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description', validators=[Length(max=500,  message='Field must be less than 500 characters.')]
     )

