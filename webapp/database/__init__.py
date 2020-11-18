import os
import sqlite3
from flask import Flask

db_file = "database/logins.db"

init_scripts = ["database/sql/create_tables.sql"]

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
for script_name in init_scripts:
    sql_file = open(script_name)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    sql_file.close()
conn.commit()
conn.close()

#Need to embed Dash within the app

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app

