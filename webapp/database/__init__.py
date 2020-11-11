import os
import sqlite3

db_file = "database/logins.db"

init_script = "database/sql/create_tables.sql"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

sql_file = open(init_script)
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)
sql_file.close()

conn.commit()
conn.close()