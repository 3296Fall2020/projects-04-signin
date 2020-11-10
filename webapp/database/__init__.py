import os
import sqlite3

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