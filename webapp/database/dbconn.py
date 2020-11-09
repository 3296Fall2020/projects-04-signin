import sqlite3

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