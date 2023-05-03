import pyodbc
from FetchLogs import ReviewLogs


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

