# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This class handles interactions with the database
# Sources:          	Project Specifications
# *****************************************************************************
import pyodbc
from FetchLogs import ReviewLogs
from datetime import datetime


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
    def get_connection(cls):
        return cls.__connection

    @classmethod
    def build_email_list(cls):
        """This method builds a list of emails from database"""

        # Define SQL call
        sql = '''
            SELECT DISTINCT EMAIL
            FROM USERS
            WHERE ROLE='subscriber';
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
            SELECT NAME, SUBJECT, MESSAGE
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
    def fetch_data(cls, start_date, end_date=None):
        """This method fetches review log data in a specified date range.
        Hakeem"""

        cls.connect()
        cursor = cls.__connection.cursor()

        if not end_date:
            end_date = datetime.now()

        query = '''
                 SELECT *FROM REVIEW_LOG
                 WHERE DATE_SENT BETWEEN ? AND ?
                 '''

        cursor.execute(query, start_date, end_date)
        rows = cursor.fetchall()
        result = []

        for row in rows:
            """This method creates/returns review logs object from data.
            Hakeem"""

            date_sent = row[3]
            review_log = ReviewLogs(row[0], row[1], row[2], date_sent, row[4])
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
        """ This method adds the user object to the DB
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        insert_user = '''
        INSERT INTO USERS(USERNAME, PASSWORD, EMAIL, FNAME, LNAME, PHONENUMBER, PREFERENCE, ROLE)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''

        cursor.execute(insert_user, (user.username, user.password, user.email, user.fname, user.lname,
                                     user.phone, user.pref, user.role))
        cursor.commit()

    @classmethod
    def login(cls, username_email):
        """ This method searches the DB for an existing user by username OR email
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        search_username_email = '''
        SELECT * FROM USERS WHERE USERNAME = ? OR EMAIL = ?
        '''

        cursor.execute(search_username_email, (username_email, username_email))
        user = cursor.fetchone()

        return user

    @classmethod
    def search_emails(cls, email):
        """ This method searches the DB for an existing email address
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        search_emails = '''
        SELECT * FROM USERS WHERE EMAIL = ?
        '''

        cursor.execute(search_emails, (email,))
        user = cursor.fetchone()

        return user

    @classmethod
    def search_usernames(cls, username):
        """ This method searches the DB for an existing username
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        search_usernames = '''
        SELECT * FROM USERS WHERE USERNAME = ?
        '''

        cursor.execute(search_usernames, (username,))
        user = cursor.fetchone()

        return user

    @classmethod
    def update_username(cls, old_username, new_username):
        """ This method updates the username in the DB
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        update_username = '''
        UPDATE USERS 
        SET USERNAME = ?
        WHERE USERNAME = ?
        '''

        cursor.execute(update_username, (new_username, old_username,))
        cursor.commit()

    @classmethod
    def update_email(cls, old_email, new_email):
        """ This method updates the email in the DB
        @author Hannah Doty """

        cls.connect()
        cursor = cls.__connection.cursor()

        update_username = '''
        UPDATE USERS 
        SET EMAIL = ?
        WHERE EMAIL = ?
        '''

        cursor.execute(update_username, (new_email, old_email,))
        cursor.commit()

    @classmethod
    def update_phone(cls, new_phone, current_username):
        """ This method updates the phone in the DB
        @author Hannah Doty"""

        cls.connect()
        cursor = cls.__connection.cursor()

        update_phone = '''
        UPDATE USERS 
        SET PHONENUMBER = ?
        WHERE USERNAME = ?
        '''

        cursor.execute(update_phone, (new_phone, current_username))
        cursor.commit()

    @classmethod
    def update_password(cls, password, current_username):
        """ This method updates the password in the DB
        @author Hannah Doty"""

        cls.connect()
        cursor = cls.__connection.cursor()

        update_password = '''
        UPDATE USERS 
        SET PASSWORD = ?
        WHERE USERNAME = ?
        '''

        cursor.execute(update_password, (password, current_username))
        cursor.commit()

    @classmethod
    def update_preference(cls, new_preference, current_username):
        """ This method updates the preference in the DB
        @author Hannah Doty"""

        cls.connect()
        cursor = cls.__connection.cursor()

        update_preference = '''
        UPDATE USERS 
        SET PREFERENCE = ?
        WHERE USERNAME = ?
        '''

        cursor.execute(update_preference, (new_preference, current_username))
        cursor.commit()

    @classmethod
    def pause_account(cls, current_username):
        """ This method changes the user preference to none in the DB
        @author Hannah Doty"""

        cls.connect()
        cursor = cls.__connection.cursor()

        update_preference = '''
        UPDATE USERS 
        SET PREFERENCE = 'none'
        WHERE USERNAME = ?
        '''

        cursor.execute(update_preference, (current_username,))
        cursor.commit()