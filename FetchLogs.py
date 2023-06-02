# *****************************************************************************
# Name:             Hakeem Hassan
# Sprint1:          Story 4
# Date:             04-25-2023
# Description:      This program fetches a list of logs in a set
# Sources:          Sprint 1 specifications
# *****************************************************************************


class ReviewLogs:
    def __init__(self, subject, message, staff, date_sent, num_subscribers):
        self.SUBJECT = subject
        self.MESSAGE = message
        self.STAFF = staff
        self.DATE_SENT = date_sent
        self.NUM_SUBSCRIBERS = num_subscribers

    @classmethod
    def from_row(cls, row):
        """This method creates/returns review logs object from data.
            Hakeem"""
        return row(
            SUBJECT=row[0],
            MESSAGE=row[1],
            STAFF=row[2],
            DATE_SENT=row[3],
            NUM_SUBSCRIBERS=row[4]
        )

    @classmethod
    def format_data(cls, data):
        """This method formats a list objects into a more readable format.
        Hakeem"""

        result = []
        for row in data:
            subject = row.SUBJECT
            message = row.MESSAGE
            staff = row.STAFF
            date_sent = row.DATE_SENT
            num_subscribers = row.NUM_SUBSCRIBERS
            formatted_row = f"{subject} - {message} - {staff} - {date_sent} - {num_subscribers}"
            result.append(formatted_row)
        return result
