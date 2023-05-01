class User:
    def __init__(self, fname, lname, email, username, password, role="subscriber"):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.role = role