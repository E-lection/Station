from e_lection import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/station')
def station():
    return render_template('station.html')
