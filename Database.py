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
    def build_template_list(cls, template):
        cls.connect()
        cursor = cls.__connection.cursor()

        insert_template = '''
        INSERT INTO TEMPLATE(NAME, SUBJECT, MESSAGE)
        VALUES (?, ?, ?)
        '''

        cursor.execute(insert_template, (template.NAME, template.SUBJECT, template.MESSAGE))
        cursor.commit()

