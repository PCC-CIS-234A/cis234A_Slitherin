# # *****************************************************************************
# # Name:             Hakeem Hassan
# # Sprint1:          Story 4
# # Date:             04-25-2023
# # Description:      This program fetches a list of logs in a set
# #                   period of dates for view.
# # Input:            fetchall or a set dates
# # Output:           displays a list of messages send
# # Sources:          Sprint 1 specifications
# # *****************************************************************************

from datetime import datetime

class ReviewLogs:
    def __init__(self, subject, message, staff, date_sent, num_subscribers):
        self.subject = subject
        self.message = message
        self.staff = staff
        self.date_sent = date_sent
        self.num_subscribers = num_subscribers

    @classmethod
    def from_row(cls, row):
        return cls(
            subject=row[0],
            message=row[1],
            staff=row[2],
            date_sent=datetime.strptime(row[3], '%Y-%m-%d'),
            num_subscribers=row[4]
        )
