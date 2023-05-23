import Validation
import unittest


class TestValidation(unittest.TestCase):

    def test_username_right_length(self):
        """If username meets length required, functions returns False"""

        username = "six ch"
        username2 = "twelve chara"

        assert not Validation.validate_username_length(username)
        assert not Validation.validate_username_length(username2)

    def test_username_no_spaces(self):
        """If username does not contain spaces, functions returns False"""

        username = "nospaces"

        assert not Validation.validate_no_spaces_username(username)

    def test_passwords_match(self):
        """If passwords match, function returns False"""

        password1 = "password"
        password2 = "password"

        assert not Validation.validate_passwords_match(password1, password2)

    def test_password_contains_special_character(self):
        """If password contains special character, function returns False"""

        password = "@"

        assert not Validation.validate_contains_special_character(password)

    def test_password_contains_number(self):
        """If password contains number, function returns False"""

        password = "1"

        assert not Validation.validate_contains_number(password)

