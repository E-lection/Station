# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

from flask import Flask, Response, redirect, url_for, request, session, abort
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user
import flask_login
from flask import Flask
from flask import render_template
from forms import FindVoterForm
from forms import LoginForm
from flask import request
from flask import flash
import urllib, urllib2
import json

import models as db
from passlib.apps import custom_app_context as pwd_context
# Configuration. Example cases for TESTING
SECRET_KEY = 'development key'

TEMPLATES_AUTO_RELOAD = True

application = Flask(__name__)
application.config.from_object(__name__)

# application.run(threaded = True)

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"

# User model
class User(UserMixin):

    def __init__(self, id, username, station_id):
        self.id = id
        self.station_id = station_id
        self.username = username

    def __repr__(self):
        return "%s/%d" % (self.username, self.station_id)

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = LoginForm(request.form)
        username = request.form['username']
        password = request.form['password']
        valid_user = get_valid_user(username, password)
        if valid_user:
            user = User(valid_user[0], username, valid_user[1])
            login_user(user)
            return redirect('')
        else:
            return render_template('login.html', message="Login unsuccessful.", form=form)
    else:
        form = LoginForm(request.form)
        return render_template('login.html', form=form)

def get_valid_user(username, password):
    users = db.retrieveUsers()
    user_id = -1
    station_id = -1
    for user in users:
        if user[1] == username:
            password_hash = user[2]
            if pwd_context.verify(password, password_hash):
                user_id = user[0]
                station_id = user[3]
                return (user_id, station_id)
            break
    return None

@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

# handle login failed
@application.errorhandler(401)
def page_not_found(e):
    return render_template('login.html', message="Login unsuccessful.", form=form)

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    users = db.retrieveUsers()
    users_with_id = filter(lambda x: x[0] == int(userid), users)
    if users_with_id:
        user = users_with_id[0]
        return User(user[0], user[1], user[3])
    else:
        return None

# Once logged in successfully, use station app to search voter
@application.route('/', methods=['GET'])
@login_required
def station():
    form = FindVoterForm(request.form)
    return render_template('station.html', form=form)

# When the clerk clicks search for voter
@application.route('/', methods=['POST'])
@login_required
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
        if success:
            # matching entry found
            return render_template('voterdb.html', voters=voters)
        else:
            # no matching entry in database, try again
            return render_template('station.html', form=form)
    return render_template('station.html', form=form)

# When the clerk clicks get pin for that voter
@application.route('/voterpincard', methods=['POST'])
@login_required
def voterpincard():
    voterid = None
    if request.method == "POST":
        voterid = request.data
        url = createPinURL(voterid)
        dbresult = urllib2.urlopen(url).read()
        resultjson = json.loads(dbresult)
        # Returned as {u'success': True, u'pin_code': 170864}
        success = resultjson['success']
        voter_pin = resultjson['pin_code']
        print ("VOTER PIN IS " + str(voter_pin))
        return render_template('voterpincard.html')
        # if success:
        #     # matching entry found
        #     return render_template('voterpincard.html', voter_pin=voter_pin)
        # else:
        #     # no matching entry in database, try again
        #     return render_template('station.html', form=form)
    return "fukd"

def createSearchURL(firstname, postcode):
    station_id = "/station_id/" + urllib.quote(str(flask_login.current_user.station_id))
    firstname = "/voter_name/" + urllib.quote(firstname)
    postcode = "/postcode/" + urllib.quote(postcode)
    url = "http://voting.eelection.co.uk/get_voters"+station_id+firstname+postcode
    return url

def createPinURL(voter_id):
    station_id = "/station_id/" + urllib.quote(str(flask_login.current_user.station_id))
    voter_id = "/voter_id/" + urllib.quote(voter_id)
    url = "http://pins.eelection.co.uk/get_pin_code" + station_id + voter_id
    return url

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
