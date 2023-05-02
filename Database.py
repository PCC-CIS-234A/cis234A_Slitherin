import pyodbc


class Database:
    __connection = None

    # Establish connection to database
    @classmethod
    def connect(cls):
        """This method connects to the database"""

        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'cis234A_Slitherin'
            username = 'cis234A_Slitherin'
            password = 'CIS234ATeamTry2!'

            cls.__connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    @classmethod
    def add_user(cls, user):
        cls.connect()
        cursor = cls.__connection.cursor()

        insert_user = '''
        INSERT INTO User_HD(First_Name, Last_Name, Username, Password, Email, Role)
        VALUES (?, ?, ?, ?, ?, ?)
        '''

        cursor.execute(insert_user, (user.fname, user.lname, user.username, user.password,  user.email, user.role))
        cursor.commit()

    @classmethod
    def login(cls, username_email):
        cls.connect()
        cursor = cls.__connection.cursor()

        search_username_email = '''
        SELECT * FROM User_HD WHERE Username = ? OR Email = ?
        '''

        cursor.execute(search_username_email, (username_email, username_email))
        user = cursor.fetchone()

        return user

    @classmethod
    def search_emails(cls, email):
        cls.connect()
        cursor = cls.__connection.cursor()

        search_emails = '''
        SELECT * FROM User_HD WHERE Email = ?
        '''

        cursor.execute(search_emails, (email,))
        user = cursor.fetchone()

        return user

    @classmethod
    def search_usernames(cls, username):
        cls.connect()
        cursor = cls.__connection.cursor()

        search_usernames = '''
        SELECT * FROM User_HD WHERE Username = ?
        '''

        cursor.execute(search_usernames, (username,))
        user = cursor.fetchone()

        return user

