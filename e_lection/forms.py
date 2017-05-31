from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class FindVoterForm(Form):
    firstname = StringField('firstname', validators=[DataRequired("No name entered.")])
    postcode = StringField('password', validators=[DataRequired("No postcode entered.")])
