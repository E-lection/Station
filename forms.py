from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

POSTCODE_REGEX = '^(?i)(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})'
NAME_REGEX = '^[A-z ,.\'-]+$'

class LoginForm(Form):
    username = StringField('username', validators=[])
    password = StringField('password', validators=[])

class FindVoterForm(Form):
    firstname = StringField('firstname', validators=[DataRequired("Error! No name entered."),
    Regexp(NAME_REGEX, message="Error! Invalid first name entered.")])
    postcode = StringField('password', validators=[DataRequired("Error! No postcode entered."),
    Regexp(POSTCODE_REGEX, message="Error! Invalid postcode entered.")])

class getVoterPin(Form):
    username = StringField('username', validators=[])
    password = StringField('password', validators=[])
