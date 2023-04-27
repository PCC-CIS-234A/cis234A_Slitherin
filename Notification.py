# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        Notification class for messages
# Sources:          	Project Specifications
# *****************************************************************************
import Database as d


class Notification:
    def __init__(self, to_addy, from_addy, subject, message, time_sent,
                 sender_id):
        self.to_addy = to_addy
        self.from_addy = from_addy
        self.subject = subject
        self.message = message
        self.time_sent = time_sent
        self.sender_id = sender_id

    @staticmethod
    def get_email_list():
        return d.Database.build_email_list()
