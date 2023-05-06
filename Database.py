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

        """This method builds a list of templates"""
    @classmethod
    def create_template(cls, name, subject, message):
        cls.connect()
        cursor = cls.__connection.cursor()

        cursor.execute("INSERT INTO TEMPLATE VALUES (?, ?, ?)",
                       name, subject, message)
        cursor.commit()

