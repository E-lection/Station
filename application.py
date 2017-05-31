# $ pip install --upgrade -r requirements.txt
# $ python -m flask run

from flask import Flask
application = Flask(__name__)

application.config['TEMPLATES_AUTO_RELOAD'] = True
application.secret_key = 'development key'

import views
import forms
