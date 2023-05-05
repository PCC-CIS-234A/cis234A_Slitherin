# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        Email class for sending emails
# Sources:          	Project Specifications
# *****************************************************************************
import smtplib
from Database import Database


class Email:
    @staticmethod
    def get_email_list():
        """This method gets a list of emails from the database"""

        return Database.build_email_list()

    @staticmethod
    def send_email(from_address, bcc, subject, body):
        """This method sends the notification - Note: Passing recipient list
        using a variable named 'bcc' automatically lists addresses as such"""

        # Define message for smtplib
        message = f"From: {from_address}\nTo: Subscribers\n" \
                  f"Subject: {subject}\n\n{body}"

        # Set variables
        smtp_server = "smtp.gmail.com"
        port = 587
        username = "PantherPantry.PCC.01@gmail.com"
        password = "tyjhruhrgbprnete"

        # Establish server and send emails
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(username, password)

            server.sendmail(from_address, bcc, message)
