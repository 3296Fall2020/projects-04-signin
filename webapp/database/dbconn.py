import sqlite3
from database.models.info_model import *

DB = "database/logins.db"

def add_login(login):
    con = sqlite3.connect(DB)
    c = con.cursor()
    # create tuple to insert into database
    insert_data = (login.first_name, login.last_name, login.gender, login.dob, login.login_time, login.reason)
    # insert data
    c.execute('INSERT INTO logins (first_name, last_name, gender, dob, login_time, reason) VALUES (?,?,?,?,?,?)', insert_data)
    con.commit()
    con.close()
    return True

def add_config(config):
    con = sqlite3.connect(DB)
    c = con.cursor()
    insert_data = (config.add_dob, config.add_gender)
    #insert data
    c.execute('UPDATE config SET add_dob = ?, add_gender = ? WHERE config_id = 1', insert_data)
    con.commit()
    con.close()
    return True

def get_config():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("SELECT * FROM config")

    config_data = c.fetchone()
    
    config = config_info(None, None, None)

    # check if config is in the database
    if config_data is None:
        c.execute("INSERT INTO config(add_dob, add_gender) VALUES ('on', 'on')")
        con.commit()
        config.confid_id = 1
        config.add_dob = 'on'
        config.add_gender = 'on'
    else:
        config.config_id, config.add_dob, config.add_gender = config_data
    
    con.close()
    return config