# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This class handles interactions with the database
# Sources:          	Project Specifications
# *****************************************************************************
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
    def build_email_list(cls):
        # Define SQL call
        sql = '''
            SELECT DISTINCT Email
            FROM User_Test;
            '''

        # Establish connection and create cursor
        cls.connect()
        cursor = cls.__connection.cursor()

        # Make SQL call to retrieve list of available email addresses
        cursor.execute(sql)
        email_list = []
        email = cursor.fetchone()

        while email:
            email_list.append(email)
            email = cursor.fetchone()

        return email_list
