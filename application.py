# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

from flask import Flask
from flask import render_template
from forms import FindVoterForm

# Configuration. Example cases for TESTING
FIRSTNAME = 'Jenny'
POSTCODE = 'B91 3LH'
SECRET_KEY = 'development key'
TEMPLATES_AUTO_RELOAD = True

application = Flask(__name__)
application.config.from_object(__name__)

@application.route('/')
def station():
    form = FindVoterForm()
    return render_template('station.html', form=form)

@application.route('/', methods=['POST'])
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
