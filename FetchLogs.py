# *****************************************************************************
# Name:             Hakeem Hassan
# Sprint1:          Story 4
# Date:             04-25-2023
# Description:      This program fetches a list of logs in a set
# Sources:          Sprint 1 specifications
# *****************************************************************************

from datetime import datetime

class ReviewLogs:
    def __init__(self, SUBJECT, MESSAGE, STAFF, DATE_SENT, NUM_SUBSCRIBERS):
        self.SUBJECT = SUBJECT
        self.MESSAGE = MESSAGE
        self.STAFF = STAFF
        self.DATE_SENT = DATE_SENT
        self.NUM_SUBSCRIBERS = NUM_SUBSCRIBERS

    @classmethod
    def from_row(cls, row):
        return row(
            SUBJECT=row[0],
            MESSAGE=row[1],
            STAFF=row[2],
            DATE_SENT=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'),
            NUM_SUBSCRIBERS=row[4]
        )

    @classmethod
    def format_data(cls, data):
        result = []
        for row in data:
            SUBJECT = row.SUBJECT
            MESSAGE = row.MESSAGE
            STAFF = row.STAFF
            DATE_SENT = row.DATE_SENT.strftime('%Y-%m-%d')
            NUM_SUBSCRIBERS = row.NUM_SUBSCRIBERS
            formatted_row = f"{SUBJECT} - {MESSAGE} - {STAFF} - {DATE_SENT} - {NUM_SUBSCRIBERS}"
            result.append(formatted_row)
        return result
