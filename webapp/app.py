#!/usr/bin/python3

from flask import Flask, render_template, request
import database
from database.models.info_model import *
from database.dbconn import *

app = Flask(__name__)

# additional input parameter booleans
add_dob = False
add_gender = False
add_organization = False

# HOME LOGIN PAGE
@app.route('/')
def home_page():
    return render_template('index.html', add_dob = add_dob, add_gender = add_gender, add_organization = add_organization)

# LOGIN FORM SUBMISSION
@app.route('/', methods=['POST'])
def submit():

    # ininitalize login_info object
    login = login_info(None, None, None, None, None, None, None)

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

    # organization
    if 'organization' in request.form:
        login.gender = request.form['organization']

    # add user input to the database
    submissionStatus = add_login(login)

    # return index html with parameters that show the form was submitted correctly
    return render_template('index.html', submitted=True, submissionStatus = submissionStatus, add_dob = add_dob, add_gender = add_gender, add_organization = add_organization)

# CONFIG PAGE
@app.route('/config')
def config_page():
    config = get_config()

    return render_template('config.html', add_dob = config.add_dob, add_gender = config.add_gender), add_organization = config.add_organization)

# CONFIG FORM SUBMISSION PAGE
@app.route('/config', methods=['POST'])
def config_page_submit():
    global add_gender
    global add_dob
    global add_organization

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

    if 'add_organization' in request.form:
        add_organization = True
        config_data.add_organization = "on"
    else:
        add_organization = False

    # add config to the database
    add_config(config_data)

    return render_template('config.html', add_dob = add_dob, add_gender = add_gender, add_organization = add_organization)

def run_app():
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
