class User:
    def __init__(self, username, password, email, fname, lname, role="subscriber"):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    @classmethod
    def create_account(cls, username, password1, email, fname, lname):
        from Database import Database
        user = User(username, password1, email, fname, lname)
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

