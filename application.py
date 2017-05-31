# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

from flask import Flask
from flask import render_template
from forms import FindVoterForm

application = Flask(__name__)

application.config['TEMPLATES_AUTO_RELOAD'] = True
application.secret_key = 'development key'

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
