from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

class LoginForm(Form):
    username = StringField('username', validators=[])
    password = StringField('password', validators=[])

class FindVoterForm(Form):
    firstname = StringField('firstname', validators=[DataRequired("Error! No name entered."),
    Regexp('^[a-zA-Z]*$', message="Error! Invalid first name entered.")])
    postcode = StringField('password', validators=[DataRequired("Error! No postcode entered."),
    Regexp('(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})', message="Error! Invalid postcode entered.")])

class getVoterPin(Form):
    username = StringField('username', validators=[])
    password = StringField('password', validators=[])
