# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This is the main UI class for Panther Pantry
# Sources:          	Project Specifications
# *****************************************************************************

from flask import Flask, render_template, redirect, url_for, request, flash, session
import Validation
from Template import Template
from Database import Database
from datetime import datetime

from User import User


class WebUI:
    """Class definition for web UI -
    View the output on localhost:5000/"""

    __app = Flask(__name__)
    __template_list = None

    def __init__(self):
        self.__app.secret_key = self.generate_key()

    @classmethod
    def get_template_list(cls):
        """This method initializes the template list from database"""

        if cls.__template_list is None:
            cls.__template_list = Template.build_list()

        return cls.__template_list

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
        """This method displays the login page"""

        return render_template("login.html")

    @staticmethod
    @__app.route('/create_account_form')
    def create_account_form():
        """This method displays the create account page"""

        return render_template("create_account_form.html")

    @staticmethod
    @__app.route("/settings")
    def settings_page():
        """This method displays the Settings page"""

        return render_template("settings.html")

    @staticmethod
    @__app.route("/landing_page")
    def index():
        """This method displays the landing page after login"""

        return render_template("landing_page.html")

    @staticmethod
    @__app.route("/create_notification")
    def create_notification():
        """This method allows the user to send a notification to
        all subscribers"""

        return render_template(
            "create_notification.html",
            template_list=WebUI.get_template_list()
        )

    @staticmethod
    @__app.route("/create_template")
    def create_template():
        """This method allows a user to create a template"""

        return render_template("create_template.html")

    @staticmethod
    def find_template(template_name):
        """This method takes a template name and returns a template object"""

        # Search template list for template
        for template in WebUI.get_template_list():
            if template.get_key() == template_name.lower():
                return template

        return None

    @staticmethod
    @__app.route("/use_template")
    def use_template():
        """This method allows the use of a template to send a notification"""

        # Find template object using name from input
        template_name = request.args['template']
        template = WebUI.find_template(template_name)

        # If no template found, raise error
        if template is None:
            return render_template(
                "error.html",
                error_message=f"There is no template named '{template_name}'"
            )

        return render_template(
            "use_template.html",
            template_name=template.get_name(),
            template_subject=template.get_subject(),
            template_text=template.get_message()
        )

    @staticmethod
    @__app.route("/send_notification")
    def send_notification():
        """This method gathers information from the UI for sending a
        notification"""

        from Notification import Notification
        from Log import Log
        from datetime import datetime

        # Collect required information
        to_addresses = Notification.get_email_list()
        to_numbers = Notification.get_phone_list()
        from_address = "PantherPantry.PCC.01@gmail.com"
        subject = request.args['subject']
        body = request.args['message']
        count = len(to_addresses) + len(to_numbers)
        time_sent = datetime.now()

        # Send emails
        Notification.send_email(
            from_address,
            to_addresses,
            subject,
            body
        )

        # Send SMS
        for num in to_numbers:
            Notification.send_sms(num, body)

        # Send notification to log
        Log.send_to_db(subject, body, 101, time_sent, count)

        return render_template(
            "send_success.html",
            subject=subject,
            time=time_sent,
            send_count=count
        )

    # Lakeys addition for date_input
    @staticmethod
    @__app.route('/review_log')
    def date_input():

        return render_template('review_log.html')

    # Lakey's addition for fetching_data
    @staticmethod
    @__app.route("/data_display")
    def fetch_data():
        """This method fetches review log data from the database within a specified date range
            Hakeem"""
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        data = Database.fetch_data(start_date=start_date, end_date=end_date)
        print('fetch_data', data)
        return render_template('data_display.html', data=data)

    # Lakey's addition for display_row
    @staticmethod
    @__app.route('/row_display/<DATE_SENT>')  # display_row
    def display_row(date_sent):
        """This method displays fetched data from the database
        Hakeem"""
        start_date = datetime.now()
        end_date = start_date
        data = Database.fetch_data(date_sent, end_date)
        return render_template('row_display.html', data=data)

    @staticmethod
    @__app.route("/add_create_template")
    def add_create_template():
        from Template import Template

        # Collect required information
        name = request.args.get('template title')
        subject = request.args.get('subject line')
        message = request.args.get('message')

        Template.add_to_db(name, subject, message)

        return render_template("save_success.html")

    @staticmethod
    @__app.route('/create_account', methods=['POST'])
    def create_account():
        """This method creates a user account
        @author Hannah Doty"""
        from User import User

        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        phone = request.form["phone"]
        pref = request.form["notification_delivery"]

        user_email = User.search_emails(email)
        user_username = User.search_usernames(username)

        if Validation.validate_username(username):
            return render_template('create_account_form.html')
        elif Validation.validate_password(password1, password2):
            return render_template('create_account_form.html')
        elif user_email:
            flash("Could not create account, please try again!", category='error')
            return render_template('create_account_form.html')
        elif user_username:
            flash("Could not create account, please try again!", category='error')
            return render_template('create_account_form.html')
        else:
            password = Validation.hash_password(password1)
            User.create_account(username, password, email, fname, lname, phone, pref)
            flash("Account Created Successfully! Please log in to your account.", category='success')
            return render_template('login.html')

    @staticmethod
    @__app.route('/login', methods=['POST'])
    def login():
        """This method logs in a user
        @author Hannah Doty"""
        from User import User
        session.pop('username', None)

        username_email = request.form["username_email_entry"]
        password = request.form["password_entry"]

        user = User.login(username_email)

        if user:
            pass_hash = user[2]
            correct_password = Validation.return_hash_password(password, pass_hash)
            if user[1] == username_email and correct_password:
                WebUI.set_session_data(user)
                return render_template('landing_page.html')
            elif user[3] == username_email and correct_password:
                WebUI.set_session_data(user)
                return render_template('landing_page.html')
            else:
                flash("Password Incorrect! Please log in again.", category='error')
                return render_template('login.html')
        else:
            flash("Username or Email Incorrect! Please log in again.", category='error')
            return render_template('login.html')

    @staticmethod
    @__app.route('/save_username', methods=['POST'])
    def save_username():
        """This method updates a users username
        @author Hannah Doty"""
        new_username = request.form['username']
        user_exists = User.search_usernames(new_username)

        if user_exists:
            flash("username already exists", category='error')
            return render_template('settings.html')
        else:
            old_username = session['username']
            Database.update_username(old_username, new_username)
            user = User.search_usernames(new_username)
            WebUI.set_session_data(user)
            return render_template('settings.html')

    @staticmethod
    @__app.route('/save_email', methods=['POST'])
    def save_email():
        """This method updates a users email
        @author Hannah Doty"""
        new_email = request.form['email']
        old_email = session['email']
        email_exists = User.search_emails(new_email)

        if email_exists:
            flash("email already exists", category='error')
            return render_template('settings.html')
        else:
            Database.update_email(old_email, new_email)
            user = User.search_emails(new_email)
            WebUI.set_session_data(user)
            return render_template('settings.html')

    @staticmethod
    @__app.route('/save_phone', methods=['POST'])
    def save_phone():
        """This method updates a users phone number
        @author Hannah Doty"""
        new_phone = request.form['phone']
        current_username = session['username']

        Database.update_phone(new_phone, current_username)
        user = User.search_usernames(current_username)
        WebUI.set_session_data(user)
        return render_template('settings.html')

    @staticmethod
    @__app.route('/save_password', methods=['POST'])
    def save_password():
        """This method updates a users password
        @author Hannah Doty"""
        new_password = request.form['password1']
        confirm_password = request.form['password2']
        current_username = session['username']

        if Validation.validate_password(new_password, confirm_password):
            flash("passwords do not match", category='error')
            return render_template('settings.html')
        else:
            password = Validation.hash_password(new_password)
            Database.update_password(password, current_username)
            user = User.search_usernames(current_username)
            WebUI.set_session_data(user)
            return render_template('settings.html')

    @staticmethod
    @__app.route('/save_preference', methods=['POST'])
    def save_preference():
        """This method updates a users notification delivery preference
        @author Hannah Doty"""
        new_preference = request.form['preference']
        current_username = session['username']

        Database.update_preference(new_preference, current_username)
        user = User.search_usernames(current_username)
        WebUI.set_session_data(user)
        return render_template('settings.html')

    @staticmethod
    @__app.route('/pause_account', methods=['POST'])
    def pause_account():
        """This method pauses a users account
        @author Hannah Doty"""
        current_username = session['username']

        Database.pause_account(current_username)
        user = User.search_usernames(current_username)
        WebUI.set_session_data(user)
        return render_template('settings.html')

    @staticmethod
    @__app.route('/delete_account', methods=['POST'])
    def delete_account():
        """This method deletes a users account
        @author Hannah Doty"""
        current_username = session['username']

        Database.delete_account(current_username)
        WebUI.destroy_session_data()
        return render_template('login.html')

    @staticmethod
    @__app.route('/unpause_account', methods=['POST'])
    def unpause_account():
        """This method unpauses a users account
        @author Hannah Doty"""
        current_username = session['username']

        Database.unpause_account(current_username)
        user = User.search_usernames(current_username)
        WebUI.set_session_data(user)
        return render_template('settings.html')

    @staticmethod
    @__app.route('/admin_user_list', methods=['POST'])
    def view_delete_user():
        """This method pulls a list of all users
        @author Hannah Doty"""
        users_list = Database.list_users()
        return render_template('edit_user.html', data=users_list)

    @staticmethod
    @__app.route('/delete_user')
    def delete_user():
        """This method deletes a users account
        @author Hannah Doty"""
        selected_username = request.args.get('username')
        Database.delete_account(selected_username)

        users_list = Database.list_users()
        return render_template('edit_user.html', data=users_list)

    @staticmethod
    @__app.route('/make_staff')
    def make_staff():
        """This method changes a users role to staff
        @author Hannah Doty"""
        selected_username = request.args.get('username')

        Database.change_role_staff(selected_username)

        users_list = Database.list_users()
        return render_template('edit_user.html', data=users_list)


    @staticmethod
    @__app.route('/make_admin')
    def make_admin():
        """This method changes a users role to admin
        @author Hannah Doty"""
        selected_username = request.args.get('username')

        Database.change_role_admin(selected_username)

        user_list = Database.list_users()
        return render_template('edit_user.html', data=user_list)

    @staticmethod
    def set_session_data(user):
        """This method sets session data for user
        @author Hannah Doty"""
        session['username'] = user[1]
        session['email'] = user[3]
        session['first_name'] = user[4]
        session['last_name'] = user[5]
        session['phone_number'] = user[6]
        session['preference'] = user[7]
        session['role'] = user[8]
        session['hidden_email'] = Validation.hide_email(user[3])
        session['hidden_phone'] = Validation.hide_phone(user[6])

    @staticmethod
    def destroy_session_data():
        """This method destroys session data for user
        @author Hannah Doty"""
        session['username'] = ''
        session['email'] = ''
        session['first_name'] = ''
        session['last_name'] = ''
        session['phone_number'] = ''
        session['email'] = ''
        session['role'] = ''
        session['hidden_email'] = ''
        session['hidden_phone'] = ''

    @staticmethod
    def run():
        """This method runs the UI"""

        WebUI.__app.run(port=5000, debug=True, ssl_context=('cert.pem', 'key.pem'))


if __name__ == "__main__":
    app = WebUI()
    app.run()
