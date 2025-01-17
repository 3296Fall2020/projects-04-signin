#!/usr/bin/python3

from flask import Flask, render_template, request
import database
import datetime
from database.models.info_model import *
from database.dbconn import *
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import json

app = Flask(__name__)

# HOME LOGIN PAGE
@app.route('/')
def home_page():
    config = get_config()

    return render_template('index.html', add_dob = config.add_dob, add_gender = config.add_gender, add_instructions = config.add_instructions, title = config.title)

# LOGIN FORM SUBMISSION
@app.route('/', methods=['POST'])
def submit():
    config = get_config()

    # ininitalize login_info object
    login = login_info(None, None, None, None, None, None, None, None)

    # add login_time to the login_info object
    login.login_time = get_current_time()

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
    
    # gender
    if 'instructions' in request.form:
        login.instructions = request.form['instructions']

    # add user input to the database
    submissionStatus = add_login(login)

    # return index html with parameters that show the form was submitted correctly
    return render_template('index.html', submitted=True, submissionStatus = submissionStatus, add_dob = config.add_dob, add_gender = config.add_gender, add_instructions = config.add_instructions, title = config.title)

# CONFIG PAGE
@app.route('/config')
def config_page():
    config = get_config()

    return render_template('config.html', add_dob = config.add_dob, add_gender = config.add_gender, add_instructions = config.add_instructions, title = config.title)

# CONFIG FORM SUBMISSION PAGE
@app.route('/config', methods=['POST'])
def config_page_submit():

    # ininitalize config info object
    config_data = config_info(None, None, None, None, None)

    # gender
    if 'add_gender' in request.form:
        config_data.add_gender = 'on'

    # dob
    if 'add_dob' in request.form:
        config_data.add_dob = 'on'

    # additional instructions
    if 'add_instructions' in request.form:
        config_data.add_instructions = 'on'

    # title
    config_data.title = request.form["title"]

    # add config to the database
    submissionStatus = add_config(config_data)

    config = get_config()

    return render_template('config.html', add_dob = config.add_dob, add_gender = config.add_gender, add_instructions = config.add_instructions, title = config.title, submissionStatus = submissionStatus)

# DATA DISPLAY PAGE
@app.route('/data')
def data_page():
    login_data = get_login()
    login_fields = get_login_fields()

    return render_template('data.html', logins = login_data, fields = login_fields)

# GRAPH PAGE
@app.route('/graph')
def graph_page():
    count = 24
    xScale = np.linspace(0, 24, count)
    yScale = get_login_times()

     # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph.html', graphJSON=graphJSON)

def run_app():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    run_app()
