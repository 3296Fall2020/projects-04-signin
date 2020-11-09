#!/usr/bin/python3

from flask import Flask, render_template, request
import database
from database.models.info_model import *
from database.dbconn import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():

    # ininitalize login_info object
    login = login_info(None, None, None, None, None, None, None)

    # error checking booleans
    nameStatus = True
    purposeStatus = True

    # retrieve parameters from html form
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    if 'purpose' in request.form:
        purpose = request.form['purpose']
        login.reason = purpose
    else:
        purposeStatus = False
        purpose = ""

    # check for correct input
    if len(firstName) == 0:
        nameStatus = False
    elif len(lastName) == 0:
        nameStatus = False
    else:
        login.first_name = firstName
        login.last_name = lastName

    print(firstName)
    print(lastName)
    print(purpose)

    # add user input to the database
    if(nameStatus and purposeStatus):
        add_login(login)

    # return index html with parameters that show the form was submitted correctly
    return render_template('index.html', submitted=True, nameStatus = nameStatus, purposeStatus = purposeStatus)

def run_app():
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
