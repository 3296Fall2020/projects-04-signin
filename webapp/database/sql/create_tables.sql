CREATE TABLE IF NOT EXISTS logins (
    login_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender TEXT,
    dob TEXT,
    login_time TEXT,
    reason TEXT NOT NULL
);