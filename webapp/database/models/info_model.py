class login_info():

    def __init__(self, login_id, first_name, last_name, gender, dob, login_time, reason, instructions):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.login_time = login_time
        self.reason = reason
        self.instructions = instructions

class config_info():

    def __init__(self, config_id, add_dob, add_gender, add_instructions, title):
        self.config_id = config_id
        self.add_dob = add_dob
        self.add_gender = add_gender
        self.add_instructions = add_instructions
        self.title = title
