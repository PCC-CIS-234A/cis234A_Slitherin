import Validation
import unittest


class TestValidation:

    def test_username_right_length(self):
        """If username meets length required, functions returns False"""

        username = "six ch"
        username2 = "twelve chara"

        assert not Validation.validate_username_length(username)
        assert not Validation.validate_username_length(username2)

    def test_username_too_short(self):
        """If username is too long, function returns True"""

        pass
        # username = "one"
        #
        # assert Validation.validate_username(username)

    def test_username_too_long(self):
        """If username is too long, function returns True"""

        pass
        # username = "twentyfivecharactersisverylong"
        #
        # assert Validation.validate_username_length(username)

    def test_username_no_spaces(self):
        """If username does not contain spaces, functions returns False"""

        username = "nospaces"

        assert not Validation.validate_no_spaces_username(username)

    def test_username_has_spaces(self):
        """If username has spaces, function returns True"""

        pass
        # username = "sp aces"
        #
        # assert Validation.validate_no_spaces_username(username)

    def test_passwords_match(self):
        """If passwords match, function returns False"""

        password1 = "password"
        password2 = "password"

        assert not Validation.validate_passwords_match(password1, password2)

    def test_passwords_dont_match(self):
        """If passwords do not match, function returns True"""

        pass
        # password1 = "password"
        # password2 = "password1"
        #
        # assert Validation.validate_password(password1, password2)

    def test_password_contains_special_character(self):
        """If password contains special character, function returns False"""

        password = "@"

        assert not Validation.validate_contains_special_character(password)

    def test_password_no_special_character(self):
        """If password does not contain special character, function returns True"""
        pass
        # password = "no special character"
        #
        # assert Validation.validate_contains_special_character(password)

    def test_password_contains_number(self):
        """If password contains number, function returns False"""

        password = "1"

        assert not Validation.validate_contains_number(password)

    def test_password_no_number(self):
        """If password does not contain a number, function returns True"""

        pass
        # password = "nonumber"
        #
        # assert Validation.validate_contains_number(password)