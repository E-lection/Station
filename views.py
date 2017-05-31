from application import application
from flask import render_template

from forms import FindVoterForm

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
