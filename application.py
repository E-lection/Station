# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

import os
import sqlite3

from flask import Flask
from flask import render_template
from forms import FindVoterForm
from flask import request
import urllib, urllib2
import json

# Configuration. Example cases for TESTING
FIRSTNAME = 'Jenny'
POSTCODE = 'B91 3LH'
SECRET_KEY = 'development key'

TEMPLATES_AUTO_RELOAD = True

application = Flask(__name__)
application.config.from_object(__name__)

application.config.update(DATABASE = os.path.join(application.root_path, 'flaskr.db'))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(application.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

@application.route('/')
def station():
    form = FindVoterForm(request.form)
    return render_template('station.html', form=form)

@application.route('/', methods=['POST'])
def find_voter():
    form = FindVoterForm(request.form)
    if form.validate_on_submit():
        firstname = request.form['firstname']
        postcode = request.form['postcode']
        url = createSearchURL(firstname, postcode)
        dbresult = urllib2.urlopen(url).read()
        resultjson = json.loads(dbresult)
        success = resultjson['success']
        voters = resultjson['voters']
        print voters
        if success:
            # matching entry found
            return render_template('voterdb.html', voters=voters)
        else:
            # no matching entry in database, try again
            return render_template('station.html', form=form)

    return render_template('station.html', form=form)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()


def createSearchURL(firstname, postcode):
    firstname = "/voter_name/" + urllib.quote(firstname)
    postcode = "/postcode/" + urllib.quote(postcode)
    url = "http://voting.eelection.co.uk/get_voters/station_id/1"+firstname+postcode
    return url

@application.route('/voterpincard')
def voterpincard():
    return render_template('voterpincard.html')
