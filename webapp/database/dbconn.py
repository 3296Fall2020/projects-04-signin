import sqlite3
from database.models.info_model import *
import datetime

DB = "database/logins.db"

def add_login(login):
    con = sqlite3.connect(DB)
    c = con.cursor()
    # create tuple to insert into database
    insert_data = (login.first_name, login.last_name, login.gender, login.dob, login.login_time, login.reason, login.instructions)
    # insert data
    c.execute('INSERT INTO logins (first_name, last_name, gender, dob, login_time, reason, instructions) VALUES (?,?,?,?,?,?,?)', insert_data)
    con.commit()
    con.close()
    return True

def get_login():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("SELECT * FROM logins")  
    # retrieve all rows from login data 
    login_data = c.fetchall()
    con.close()
    return login_data

def get_login_fields():
    fields = ["ID", "First Name", "Last Name", "Gender", "Date of Birth", "Login Time", "Reason for Visit", "Additional Instructions"]
    return fields

def add_config(config):
    con = sqlite3.connect(DB)
    c = con.cursor()
    insert_data = (config.add_dob, config.add_gender, config.add_instructions, config.title)
    #insert data
    c.execute('UPDATE config SET add_dob = ?, add_gender = ?, add_instructions = ?, title = ? WHERE config_id = 1', insert_data)
    con.commit()
    con.close()
    return True

def get_config():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("SELECT * FROM config")

    config_data = c.fetchone()
    
    config = config_info(None, None, None, None, None)

    # check if config is in the database
    if config_data is None:
        c.execute("INSERT INTO config(add_dob, add_gender, add_instructions, title) VALUES ('on', 'on', 'on', 'Welcome')")
        con.commit()
        config.confid_id = 1
        config.add_dob = 'on'
        config.add_gender = 'on'
        config.add_instructions = 'on'
        config.title = 'Welcome'
    else:
        config.config_id, config.add_dob, config.add_gender, config.add_instructions, config.title = config_data
    
    con.close()
    return config

def get_current_time():
    current_time = datetime.datetime.now()
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    month = str(current_time.month)
    day = str(current_time.day)
    year = str(current_time.year)
    login_time = hour + ":" + minute + " " + month + "/" + day + "/" + year
    return login_time

def get_login_times():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("SELECT login_time FROM logins")  
    # retrieve login times 
    login_times = c.fetchall()
    con.close()
    #format hour times in an array
    times = []
    for time in login_times:
        times.append(time[0][:2])
    
    #calculate time frequency
    time_count = {}
    for time in times:
        if time in time_count:
            time_count[time] += 1
        else:
            time_count[time] = 1
    
    times = []
    for i in range(0, 24):
        if str(i) in time_count:
            times.append(time_count[str(i)])
        else:
            times.append(0)

    return times