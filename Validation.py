from flask import flash, render_template


def validate_username_length(username):
    if len(username) < 8:
        flash("Invalid username length, must be 8 characters long!", category='error')
        return render_template('create_account_form.html')


def validate_no_spaces(username):
    if ' ' in username:
        flash("Username cannot contain spaces!", category='error')
        return render_template('create_account_form.html')


def validate_passwords_match(password1, password2):
    if password1 != password2:
        flash("Passwords do not match. Try again!", category='error')
        return render_template('create_account_form.html')


def validate_password_length(password1):
    if len(password1) < 8:
        flash("Invalid password length, must be 8 characters long!", category='error')
        return render_template('create_account_form.html')
