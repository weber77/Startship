from datetime import date, datetime

class loginModel:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class signupModel:
    def __init__(self, username, password, email, address, role):
        self.name = username
        self.password = password
        self.email = email
        self.address = address
        self.role = role
        self.login_status = 0
        self.register_date = str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

