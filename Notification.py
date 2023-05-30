# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        Email class for sending emails
# Sources:          	Project Specifications
# *****************************************************************************
import smtplib
from Database import Database


class Notification:
    @staticmethod
    def get_email_list():
        """This method gets a list of emails from the database"""

        return Database.build_email_list()

    @staticmethod
    def get_phone_list():
        """This method gets a list of emails from the database"""

        return Database.build_phone_list()

    @staticmethod
    def send_email(from_address, bcc, subject, body):
        """This method sends the notification"""

        # Define message for smtplib
        message = f"From: Panther Pantry\nTo: Subscribers\n" \
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

            # Passing recipient list using a variable named 'bcc'
            # automatically sends to given addresses as such
            server.sendmail(from_address, bcc, message)

    @staticmethod
    def send_sms(number, body):
        from twilio.rest import Client

        account_sid = "AC0afd914d5be65b0873ed7a832a9c0f6c"
        auth_token = "d9ed081e90525c4f328e2e9371350557"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body,
            from_="+18883781722",
            to=number
        )

        print(message.sid)


# msg = "This is a test of the dumb broadcast system"
# numbers = ["9713716946", "5038751835"]
# # for num in numbers:
# #     Email.send_sms(num, msg)
# Notification.send_email("PantherPantry.PCC.01@gmail.com", numbers, "Test", msg)
