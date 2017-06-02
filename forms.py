from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

class FindVoterForm(Form):
    firstname = StringField('firstname', validators=[DataRequired("No name entered."),
    Regexp('[A-Za-z\'-]+', message="Invalid first name entered")])
    postcode = StringField('password', validators=[DataRequired("No postcode entered."),
    Regexp('(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})', message="Invalid postcode entered")])

class LoginForm(Form):
    username = StringField('username', validators=[])
    password = StringField('password', validators=[])
# db = SQLAlchemy()

# class User(db.Model):
#     """An admin user capable of viewing reports.
#
#     :param str email: email address of user
#     :param str password: encrypted password for the user
#
#     """
#     __tablename__ = 'user'
#
#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String)
#     authenticated = db.Column(db.Boolean, default=False)
#
#     def is_active(self):
#         """True, as all users are active."""
#         return True
#
#     def get_id(self):
#         """Return the email address to satisfy Flask-Login's requirements."""
#         return self.email
#
#     def is_authenticated(self):
#         """Return True if the user is authenticated."""
#         return self.authenticated
#
#     def is_anonymous(self):
#         """False, as anonymous users aren't supported."""
#         return False
