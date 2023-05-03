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
        """This method builds a list of email from database entries"""

        # Define SQL call
        sql = '''
            SELECT DISTINCT EMAIL
            FROM USER_ID
            WHERE ROLE='Subscriber';
            '''

        # Establish connection and create cursor
        cls.connect()
        cursor = cls.__connection.cursor()

        # Make SQL call to retrieve list of available email addresses
        cursor.execute(sql)
        email_list = []
        email = cursor.fetchone()

        # Build the email list
        while email:
            email_list.append(email[0])
            email = cursor.fetchone()

        return email_list

    @classmethod
    def add_log(cls, subject, body, sender_id, time_sent, count):
        """This method adds a log object to the database"""

        # Define SQL call
        # sql = "INSERT INTO Review_log VALUES (%s, %s, %s, %s, %s)", \
        #    subject, body, sender_id, time_sent, count

        # Establish connection and add notification to the log
        subject = subject

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute("INSERT INTO Review_log VALUES (?, ?, ?, ?, ?)",
                       subject, body, sender_id, time_sent, count)
        cursor.commit()
