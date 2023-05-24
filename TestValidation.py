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
        username2 = "anothernospace"

        assert not Validation.validate_no_spaces_username(username)
        assert not Validation.validate_no_spaces_username(username2)

    def test_passwords_match(self):
        """If passwords match, function returns False"""

        password1 = "password"
        password2 = "password"

        password3 = "matching"
        password4 = "matching"

        assert not Validation.validate_passwords_match(password1, password2)
        assert not Validation.validate_passwords_match(password3, password4)

    def test_password_contains_special_character(self):
        """If password contains special character, function returns False"""

        password = "@"
        password2 = "pas!"

        assert not Validation.validate_contains_special_character(password)
        assert not Validation.validate_contains_special_character(password2)

    def test_password_contains_number(self):
        """If password contains number, function returns False"""

        password = "1"
        password2 = "m4"

        assert not Validation.validate_contains_number(password)
        assert not Validation.validate_contains_number(password2)

    def test_password_no_number(self):
        """If password does not contain a number, function returns True"""
        # Override flash
        my_flash = Validation.flash
        Validation.flash = lambda *vargs, **kwargs: None

        password = "nonumber"
        password2 = "number?no"
        
        assert Validation.validate_contains_number(password)
        assert Validation.validate_contains_number(password2)

        # Undo Override
        Validation.flash = my_flash

    def test_username_too_short(self):
        """If username is too long, function returns True"""
        # Override flash
        my_flash = Validation.flash
        Validation.flash = lambda *vargs, **kwargs: None

        username = "one"
        username2 = "to"

        assert Validation.validate_username_length(username)
        assert Validation.validate_username_length(username2)
        # Undo Override
        Validation.flash = my_flash

    def test_username_has_spaces(self):
        """If username has spaces, function returns True"""
        # Override flash
        my_flash = Validation.flash
        Validation.flash = lambda *vargs, **kwargs: None

        username = "sp aces"
        username2 = "a space"

        assert Validation.validate_no_spaces_username(username)
        assert Validation.validate_no_spaces_username(username2)

        # Undo Override
        Validation.flash = my_flash

    def test_password_no_special_character(self):
        """If password does not contain special character, function returns True"""
        # Override flash
        my_flash = Validation.flash
        Validation.flash = lambda *vargs, **kwargs: None

        password = "no special character"
        password2 = "specialwut"

        assert Validation.validate_contains_special_character(password)
        assert Validation.validate_contains_special_character(password2)

        # Undo Override
        Validation.flash = my_flash
