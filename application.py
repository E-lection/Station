# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

from flask import Flask
application = Flask(__name__)

application.config['TEMPLATES_AUTO_RELOAD'] = True
application.secret_key = 'development key'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp
from flask import render_template

class FindVoterForm(Form):
    firstname = StringField('firstname', validators=[DataRequired("No name entered."),
    Regexp('/^[a-z ,.\'-]+$/i', message="Invalid first name entered")])
    postcode = StringField('password', validators=[DataRequired("No postcode entered."),
    Regexp('(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})', message="Invalid postcode entered")])

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/station')
def station():
    form = FindVoterForm()
    return render_template('station.html', form=form)

@application.route('/station', methods=['POST'])
def find_voter():
    form = FindVoterForm()
    if form.validate_on_submit():
        return render_template('voterdb.html', form=form)
    return render_template('station.html', form=form)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
