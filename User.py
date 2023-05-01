class User:
    def __init__(self, fname, lname, email, username, password, role="subscriber"):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    @classmethod
    def create_account(cls, fname, lname, email, username, password1):
        from Database import Database
        user = User(fname, lname, email, username, password1)
        Database.add_user(user)

