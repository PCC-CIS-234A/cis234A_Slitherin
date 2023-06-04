import bcrypt
from flask import flash, render_template


def validate_username_length(username):
    """ This method validates username is between 5 and 25 characters
    @author Hannah Doty """

    if len(username) <= 5:
        flash("Invalid username length, must be 5 characters long!", category='error')
        return True
    elif len(username) > 25:
        flash("Invalid username length, cannot be more than 25 characters long")
        return True


def validate_no_spaces_username(username):
    """ This method validates username contains no spaces
    @author Hannah Doty """

    if ' ' in username:
        flash("Username cannot contain spaces!", category='error')
        return True


def validate_no_spaces_password(password1):
    """ This method validates password contains no spaces
    @author Hannah Doty """

    if ' ' in password1:
        flash("Password cannot contain spaces!", category='error')
        return True


def validate_passwords_match(password1, password2):
    """ This method validates password match
    @author Hannah Doty """

    if password1 != password2:
        flash("Passwords do not match. Try again!", category='error')
        return True


def validate_password_length(password1):
    """ This method validates password is correct length
    @author Hannah Doty """

    if len(password1) < 8:
        flash("Invalid password length, must be 8 characters long!", category='error')
        return True


def validate_contains_number(password1):
    """ This method validates password contains a number
    @author Hannah Doty """

    if any(char.isdigit() for char in password1):
        return False
    else:
        flash("Password must contain a number!", category='error')
        return True


def validate_contains_special_character(password1):
    """ This method validates password contains a special character
    @author Hannah Doty """

    special_characters = ["!", "@", "#", '$', "%", "^", "&", "*"]
    if any(c in special_characters for c in password1):
        return False
    else:
        flash("Password must contain a special character! (!, @, #, $, %, ^, &, *)", category='error')
        return True


def validate_username(username):
    """ This method validates username meets all requirements
    @author Hannah Doty """
    if validate_username_length(username):
        return render_template('create_account_form.html')
    elif validate_no_spaces_username(username):
        return render_template('create_account_form.html')
    else:
        return False


def validate_password(password1, password2):
    """ This method validates password meets all requirements
    @author Hannah Doty """
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
    """ This method hashes clear text password
    @author Hannah Doty """
    password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt(12))
    return password


def return_hash_password(password1, password):
    """ This method compares user entered password to stored password
    @author Hannah Doty """
    pass_hash = bcrypt.checkpw(password1.encode('utf-8'), password.encode('utf-8'))
    return pass_hash


def hide_email(email):
    """ This method hides part of the email address
    @author Hannah Doty """
    email_split = email.split('@')
    email_part1 = email_split[0]
    email_part2 = email_split[1]

    half = int(len(email_part1) / 2)
    hidden_email = ('*' * half) + email_part1[-half:] + '@' + email_part2
    return hidden_email


def hide_phone(phone):
    """ This method hides part of the phone number
    @author Hannah Doty """

    end = phone[-4:]
    return '***-***-' + end

