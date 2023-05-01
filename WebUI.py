from flask import Flask, render_template, redirect, url_for, request, flash

import Validation
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
    @__app.route("/login")
    def homepage():
        """This method displays the homepage"""

        return render_template("login.html")

    @staticmethod
    @__app.route('/create_account_form')
    def create_account_form():
        """This method displays the create account page"""

        return render_template("create_account_form.html")

    @staticmethod
    @__app.route("/landing_page")
    def index():
        """This method displays the landing page after login"""

        return render_template("landing_page.html")

    @staticmethod
    @__app.route("/under_construction.html")
    @__app.route("/under_construction")
    def under_con():
        return render_template("under_construction.html")

    @staticmethod
    @__app.route("/create_notification")
    def send_notification():
        """This method allows the user to send a food availability
        notification to all subscribers"""

        # TODO: REMOVE TEST CODE

        return render_template("create_notification.html", template_list=WebUI.__template_list)

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

        return render_template("use_template.html", template=template)

    @staticmethod
    @__app.route("/send_notification")
    def send_not():
        subject = request.args['subject']
        msg = request.args['message']

        # TODO: ADD SEND FUNCTION HERE AND ASK HOW TO GET MESSAGE (cont)
        # TODO: WITHOUT THE ENTIRE MESSAGE TEXT BEING IN THE URL - POST METHOD?

        return render_template("send_success.html", subject=subject)

    @staticmethod
    @__app.route("/send_success")
    def send_success():
        # TODO: ADD TO LOG HERE
        template = request.args["subject"]

        return render_template("send_success.html")

    @staticmethod
    @__app.route("/review_log")
    def view_log():
        """This method allows a user to view the notification log"""

        return render_template("under_construction.html")

    @staticmethod
    @__app.route('/create_account', methods=['POST'])
    def create_account():
        from User import User

        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        user_email = User.search_emails(email)
        user_username = User.search_usernames(username)

        if Validation.validate_username_length(username):
            return render_template('create_account_form.html')
        elif Validation.validate_no_spaces(username):
            return render_template('create_account_form.html')
        elif user_email:
            flash("Email already in use!", category='error')
            return render_template('create_account_form.html')
        elif user_username:
            flash("Username already in use!", category='error')
            return render_template('create_account_form.html')
        elif password1 != password2:
            flash("Passwords do not match. Try again!", category='error')
            return render_template('create_account_form.html')
        else:
            User.create_account(fname, lname, email, username, password1)
            flash("Account Created Successfully! Please log in to your account.", category='success')
            return render_template('login.html')

    @staticmethod
    @__app.route('/login', methods=['POST'])
    def login():
        from User import User

        username_email = request.form["username_email_entry"]
        password = request.form["password_entry"]
        user = User.login(username_email, password)
        if user:
            if user[1] == username_email and user[2] == password:
                return render_template('landing_page.html')
            elif user[3] == username_email and user[2] == password:
                return render_template('landing_page.html')
        else:
            flash("Username/Email or Password Incorrect! Please log in again.", category='error')
            return render_template('login.html')

    @staticmethod
    def run():
        """This method runs the UI"""

        WebUI.__app.run(port=5000)


if __name__ == "__main__":
    app = WebUI()
    app.run()
