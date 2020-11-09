class login_info():

    def __init__(self, login_id, first_name, last_name, gender, dob, login_time, reason):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.login_time = login_time
        self.reason = reason

    def __getitem__(self, key):
        return getattr(self, key)