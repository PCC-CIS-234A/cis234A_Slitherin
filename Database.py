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
