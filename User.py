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

    @classmethod
    def login(cls, username_email):
        from Database import Database
        user = Database.login(username_email)
        return user

    @classmethod
    def search_emails(cls, email):
        from Database import Database
        user = Database.search_emails(email)
        return user

    @classmethod
    def search_usernames(cls, username):
        from Database import Database
        user = Database.search_usernames(username)
        return user

