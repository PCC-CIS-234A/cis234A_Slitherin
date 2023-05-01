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

