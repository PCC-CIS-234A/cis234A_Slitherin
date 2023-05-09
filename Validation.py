import bcrypt
from flask import flash, render_template


def validate_username_length(username):
    if len(username) < 5:
        flash("Invalid username length, must be 5 characters long!", category='error')
        return True
    elif len(username) > 25:
        flash("Invalid username length, cannot be more than 25 characters long")
        return True


def validate_no_spaces_username(username):
    if ' ' in username:
        flash("Username cannot contain spaces!", category='error')
        return True


def validate_no_spaces_password(password1):
    if ' ' in password1:
        flash("Password cannot contain spaces!", category='error')
        return True


def validate_passwords_match(password1, password2):
    if password1 != password2:
        flash("Passwords do not match. Try again!", category='error')
        return True


def validate_password_length(password1):
    if len(password1) < 8:
        flash("Invalid password length, must be 8 characters long!", category='error')
        return True


def validate_contains_number(password1):
    if any(char.isdigit() for char in password1):
        return False
    else:
        flash("Password must contain a number!", category='error')
        return True


def validate_contains_special_character(password1):
    special_characters = ["!", "@", "#", '$', "%", "^", "&", "*"]
    if any(c in special_characters for c in password1):
        return False
    else:
        flash("Password must contain a special character! (!, @, #, $, %, ^, &, *)", category='error')
        return True


def validate_username(username):
    if validate_username_length(username):
        return render_template('create_account_form.html')
    elif validate_no_spaces_username(username):
        return render_template('create_account_form.html')
    else:
        return False


def validate_password(password1, password2):
    if validate_passwords_match(password1, password2):
        return render_template('create_account_form.html')
    elif validate_password_length(password1):
        return render_template('create_account_form.html')
    elif validate_no_spaces_password(password1):
        return render_template('create_account_form.html')
    elif validate_contains_number(password1):
        return render_template('create_account_form.html')
    elif validate_contains_special_character(password1):
        return render_template('create_account_form.html')
    else:
        return False


def hash_password(password1):
    password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt(12))
    return password


def return_hash_password(password1, password):
    pass_hash = bcrypt.checkpw(password1.encode('utf-8'), password.encode('utf-8'))
    return pass_hash
