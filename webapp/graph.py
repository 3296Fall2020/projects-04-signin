from flask import Flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html


server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash'
)

app.layout = html.Div(id='dash-container')

@server.route("/dash")
def my_dash_app():
    return app.index()

#Dash inside Flask method
#/plotlydash-flask-tutorial
#├── /plotlyflask_tutorial
#│   ├── __init__.py
#│   ├── routes.py
#│   ├── /static
#│   ├── /templates
#│   └── /plotlydash
#│       └── dashboard.py
#├── /data
#├── README.md
#├── config.py
#├── requirements.txt
#├── start.sh
#└── wsgi.py

