# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This class handles interactions with the database
# Sources:          	Project Specifications
# *****************************************************************************
import pyodbc
from FetchLogs import ReviewLogs


class Database:
    __connection = None

    # Establish connection to database
    @classmethod
    def connect(cls):
        """This method connects to the database"""

        # Set connection variables
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'cis234A_Slitherin'
            username = 'cis234A_Slitherin'
            password = 'CIS234ATeamTry2!'

            # Set connection string
            cls.__connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    @classmethod
    def build_email_list(cls):
        """This method builds a list of emails from database"""

        # Define SQL call
        sql = '''
            SELECT DISTINCT EMAIL
            FROM USER_ID
            WHERE ROLE='Subscriber';
            '''

        # Establish connection and create cursor
        cls.connect()
        cursor = cls.__connection.cursor()

        # Make SQL call to retrieve list of email addresses
        cursor.execute(sql)
        email_list = []
        email = cursor.fetchone()

        # Build the email list
        while email:
            email_list.append(email[0])
            email = cursor.fetchone()

        return email_list

    @classmethod
    def build_template_list(cls):
        """This method builds a list of templates from database"""

        from Template import Template

        # Define SQL call
        sql = '''
            SELECT *
            FROM TEMPLATE;
            '''

        # Establish connection and create cursor
        cls.connect()
        cursor = cls.__connection.cursor()

        # Make SQL call to retrieve list of available templates
        cursor.execute(sql)
        template_list = []
        template = cursor.fetchone()

        # Build the template list
        while template:
            template = Template(template[0], template[1], template[2])
            template_list.append(template)
            template = cursor.fetchone()

        return template_list

    @classmethod
    def add_log(cls, subject, body, sender_id, time_sent, count):
        """This method adds each notification to the Log database"""

        # Establish connection and create cursor
        cls.connect()
        cursor = cls.__connection.cursor()

        # Add to log
        cursor.execute("INSERT INTO REVIEW_LOG VALUES (?, ?, ?, ?, ?)",
                       subject, body, sender_id, time_sent, count)
        cursor.commit()

    # Lakey's fetch_data classmethod
    @classmethod
    def fetch_data(cls, start_date, end_date):
        cls.connect()
        cursor = cls.__connection.cursor()

        query = '''
            SELECT * FROM Review_log 
            WHERE Date_sent 
            BETWEEN ? 
            AND ?
            '''
        cursor.execute(query, start_date, end_date)
        rows = cursor.fetchall()
        result = []

        for row in rows:
            review_log = ReviewLogs.from_row(row)
            result.append(review_log)

        return result

    @classmethod
    def create_template(cls, name, subject, message):
        cls.connect()
        cursor = cls.__connection.cursor()

        cursor.execute("INSERT INTO TEMPLATE VALUES (?, ?, ?)",
                       name, subject, message)
        cursor.commit()

    @classmethod
    def add_user(cls, user):
        cls.connect()
        cursor = cls.__connection.cursor()

        insert_user = '''
        INSERT INTO User_HD(Username, Password, Email, First_Name, Last_Name, Role)
        VALUES (?, ?, ?, ?, ?, ?)
        '''

        cursor.execute(insert_user, (user.username, user.password, user.email, user.fname, user.lname, user.role))
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



