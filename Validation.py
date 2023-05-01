from flask import flash, render_template


def validate_username_length(username):
    if len(username) < 8:
        flash("Invalid username length, must be 8 characters long!", category='error')
        return render_template('create_account_form.html')
