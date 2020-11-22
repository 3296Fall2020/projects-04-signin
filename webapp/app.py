#!/usr/bin/python3

from flask import Flask, render_template, request
import database
import datetime
from database.models.info_model import *
from database.dbconn import *

app = Flask(__name__)

add_dob = False
add_gender = False

# HOME LOGIN PAGE
@app.route('/')
def home_page():
    config = get_config()

    return render_template('index.html', add_dob = config.add_dob, add_gender = config.add_gender)

# LOGIN FORM SUBMISSION
@app.route('/', methods=['POST'])
def submit():
    config = get_config()

    # ininitalize login_info object
    login = login_info(None, None, None, None, None, None, None)

    # add login_time to the login_info object
    current_time = datetime.datetime.now()
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    month = str(current_time.month)
    day = str(current_time.day)
    year = str(current_time.year)
    login_time = hour + ":" + minute + " " + month + "/" + day + "/" + year
    login.login_time = login_time

    # retrieve parameters from html form

    # name
    login.first_name = request.form['firstName']
    login.last_name = request.form['lastName']

    # reason for visit

    login.reason = request.form['purpose']


    # date of birth
    if 'dob' in request.form:
        login.dob = request.form['dob']

    # gender
    if 'gender' in request.form:
        login.gender = request.form['gender']

    # add user input to the database
    submissionStatus = add_login(login)

    # return index html with parameters that show the form was submitted correctly
    return render_template('index.html', submitted=True, submissionStatus = submissionStatus, add_dob = config.add_dob, add_gender = config.add_gender)

# CONFIG PAGE
@app.route('/config')
def config_page():
    config = get_config()

    return render_template('config.html', add_dob = config.add_dob, add_gender = config.add_gender)

# CONFIG FORM SUBMISSION PAGE
@app.route('/config', methods=['POST'])
def config_page_submit():
    global add_gender
    global add_dob

    # ininitalize config info object
    config_data = config_info(None, None, None)

    if 'add_gender' in request.form:
        add_gender = True
        config_data.add_gender = 'on'
    else: 
        add_gender = False

    if 'add_dob' in request.form:
        add_dob = True
        config_data.add_dob = 'on'
    else:
        add_dob = False

    # add config to the database
    add_config(config_data)

    return render_template('config.html', add_dob = add_dob, add_gender = add_gender)

# DATA DISPLAY PAGE
@app.route('/data')
def data_page():
    login_data = get_login()
    login_fields = get_login_fields()

    return render_template('data.html', logins = login_data, fields = login_fields)


def run_app():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    run_app()
