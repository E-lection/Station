from e_lection import app
from flask import render_template
from flask import request

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/station')
def station():
    return render_template('station.html')

@app.route('/station', methods=['POST'])
def my_form_post():
    firstname = request.form['firstname']
    postcode = request.form['postcode']
    return firstname
