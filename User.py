class User:
    """ Class Definition for the User Object
    @author Hannah Doty
    @param username
    @param password
    @param email
    @param fname First name
    @param lname Last name
    @param role User role (default value is subscriber)"""
    def __init__(self, username, password, email, fname, lname, phone="1234567891", pref="email", role="subscriber"):
        self.username = username
        self.password = password
        self.email = email
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.pref = pref
        self.role = role

    @classmethod
    def create_account(cls, username, password1, email, fname, lname, phone, pref):
        """ This method creates a user object and passes it to the add_user DB method
        @author Hannah Doty """

        from Database import Database
        user = User(username, password1, email, fname, lname, phone, pref)
        Database.add_user(user)

    @classmethod
    def login(cls, username_email):
        """ This method passes username or email entry to the login DB method
        @author Hannah Doty """

        from Database import Database
        user = Database.login(username_email)
        return user

    @classmethod
    def search_emails(cls, email):
        """ This method passes the email entry to the search_emails DB method
        @author Hannah Doty """

        from Database import Database
        user = Database.search_emails(email)
        return user

    @classmethod
    def search_usernames(cls, username):
        """ This method passes the username entry to the search_usernames DB method
        @author Hannah Doty """

        from Database import Database
        user = Database.search_usernames(username)
        return user

