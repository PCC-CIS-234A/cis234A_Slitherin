# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        Log class for handling logging functions
# Sources:          	Project Specifications
# *****************************************************************************
from Database import Database


class Log:
    def __init__(self, subject, message, sender_id, time_sent, count):
        self.subject = subject
        self.message = message
        self.sender_id = sender_id
        self.time_sent = time_sent
        self.send_count = count

    @staticmethod
    def send_to_db(subject, body, sender_id, time_sent, count):
        Database.add_log(subject, body, sender_id, time_sent, count)
