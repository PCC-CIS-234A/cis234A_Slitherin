# *****************************************************************************
# Name:             Hakeem Hassan
# Sprint1:          Story 4
# Date:             04-25-2023
# Description:      This program fetches a list of logs in a set
#                   period of dates for view.
# Input:            fetchall or a set dates
# Output:           displays a list of messages send
# Sources:          Sprint 1 specifications
# *****************************************************************************

from flask import Flask, render_template, request
import pyodbc
from datetime import datetime




class Database:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'tcp:cisdbss.pcc.edu'
    database = 'cis234A_Slitherin'
    username = 'cis234A_Slitherin'
    password = 'CIS234ATeamTry2!'

    @staticmethod
    def connect(conn_str):
        conn = pyodbc.connect(conn_str)
        return conn

    @staticmethod
    def disconnect(conn):
        conn.close()

    @staticmethod
    def fetch_data(start_date, end_date):
        conn_str = f"DRIVER={Database.driver};" \
                   f"SERVER={Database.server};" \
                   f"DATABASE={Database.database};" \
                   f"UID={Database.username};" \
                   f"PWD={Database.password}"
        conn = Database.connect(conn_str)
        cursor = conn.cursor()


        query = f"SELECT * FROM Review_log " \
                f"WHERE Date_sent " \
                f"BETWEEN '{start_date}' " \
                f"AND '{end_date}'"
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []

        for row in rows:
            result.append({
                'subject': row[0],
                'message': row[1],
                'staff': row[2],
                'date_sent': datetime.strptime(row[3], '%Y-%m-%d'),
                'num_subscribers': row[4]
            })

        cursor.close()
        Database.disconnect(conn)

        return result


app = Flask(__name__)


# Made copy to WebUI section
#
# @app.route('/')
# def date_input():
#     return render_template('review_log.html')
#
#
# @app.route('/fetch_data')
# def fetch_data():
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')
#     data = Database.fetch_data(start_date, end_date)
#     return render_template('data_display.html', data=data)

