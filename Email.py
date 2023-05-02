# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        Email class for sending emails
# Sources:          	Project Specifications
# *****************************************************************************
import smtplib


class Email:

    @staticmethod
    def send_email(from_address, to_addresses, subject, body):
        """This method sends the notification"""

        message = f"From: {from_address}\nTo: Subscribers\n" \
                  f"Subject: {subject}\n\n{body}"

        smtp_server = "smtp.gmail.com"
        port = 587
        username = "PantherPantry.PCC.01@gmail.com"
        password = "tyjhruhrgbprnete"

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(username, password)

            server.sendmail(from_address, to_addresses, message)
