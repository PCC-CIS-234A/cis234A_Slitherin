# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This is the main UI class for Panther Pantry
# Sources:          	Project Specifications
# *****************************************************************************
from flask import Flask, render_template, redirect, url_for, request
from Template import Template


class WebUI:
    """Class definition for web UI -
    View the output on localhost:5000/"""

    __app = Flask(__name__)
    __template_list = Template.build_list()

    def __init__(self):
        self.__app.secret_key = self.generate_key()

    @staticmethod
    def generate_key():
        """This method generates a cryptographically random session key"""

        import os

        return os.urandom(6)

    @staticmethod
    @__app.route("/menu")
    @__app.route("/home")
    @__app.route("/default")
    @__app.route("/default.html")
    def redirect_to_menu():
        """This method redirects common homepage URLs to homepage"""

        return redirect(url_for("homepage"))

    @staticmethod
    @__app.route("/")
    def homepage():
        """This method displays the homepage"""

        return render_template("login.html")

    @staticmethod
    @__app.route("/landing_page")
    def index():
        """This method displays the landing page after login"""

        return render_template("landing_page.html")

    @staticmethod
    @__app.route("/under_construction")
    def under_construction():
        """This method displays the construction page"""

        return render_template("under_construction.html")

    @staticmethod
    @__app.route("/create_notification")
    def create_notification():
        """This method allows the user to send a food availability
        notification to all subscribers"""

        return render_template(
            "create_notification.html",
            template_list=WebUI.__template_list
        )

    @staticmethod
    @__app.route("/create_template")
    def create_template():
        """This method allows a user to create a template"""

        return render_template("under_construction.html")

    @staticmethod
    def find_template(template_name):
        """This method takes a list name and returns a list object"""

        for template in WebUI.__template_list:
            if template.get_key() == template_name.lower():
                return template

        return None

    @staticmethod
    @__app.route("/use_template")
    def use_template():
        """This method allows the use of a Template to send a notification"""

        template_name = request.args['template']
        template = WebUI.find_template(template_name)

        if template is None:
            return render_template(
                "error.html",
                error_message=f"There is no template named '{template_name}'"
            )

        return render_template(
            "use_template.html",
            template_name=template.get_name(),
            template_subject=template.get_subject(),
            template_text=template.get_text()
        )

    @staticmethod
    @__app.route("/send_notification")
    def send_notification():
        """This method gathers information from the UI for sending a
        notification"""

        from Email import Email
        from Notification import Notification

        # Collect required information from UI
        emails = Notification.get_email_list()
        email_list = ", ".join(emails)
        subject = request.args['subject']
        body = request.args['message']
        count = len(emails)

        # Call the method to send emails
        Email.send_email(
            "PantherPantry.PCC.01@gmail.com",
            emails,
            subject,
            body
        )

        return render_template(
            "send_success.html",
            subject=subject,
            message=body,
            send_count=count,
            email_list=email_list
        )

    @staticmethod
    @__app.route("/send_success")
    def send_success():
        """This method renders the 'Send Success' page"""
        # TODO: ADD TO LOG HERE

        return render_template("send_success.html")

    @staticmethod
    @__app.route("/review_log")
    def view_log():
        """This method allows a user to view the notification log"""

        return render_template("under_construction.html")

    @staticmethod
    def run():
        """This method runs the UI"""

        # TODO: REMOVE HOST ARGUMENT
        WebUI.__app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    app = WebUI()
    app.run()
