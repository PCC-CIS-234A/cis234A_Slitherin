import unittest
from Database import Database
from WebUI import WebUI


class TestDB(unittest.TestCase):
    """This method tests various methods in the Database class
    Numeric values should be changed to reflect database changes"""

    def test_connection(self):
        """Test the database connection"""

        Database.connect()
        assert Database.get_connection() is not None

    def test_build_template_list(self):
        """Test the template list - Value should be edited as the size changes
        I know that this is not a good test, but there aren't many
        methods that I wrote that are testable"""

        template_list = Database.build_template_list()
        assert template_list is not None

    def test_build_email_list(self):
        """Test the template list - Value should be edited as the size changes
        I know that this is not a good test, but there aren't many
        methods that I wrote that are testable"""

        email_list = Database.build_email_list()
        assert email_list is not None


class TestKey(unittest.TestCase):
    def test_generate_key(self):
        """This method defines test for key generation"""

        # Call the generate_key method
        key = WebUI.generate_key()

        # Assert that the key is not None
        self.assertIsNotNone(key)

    def test_key_random(self):
        """This method tests that the key is random"""

        # Generate two keys
        key = WebUI.generate_key()
        key2 = WebUI.generate_key()

        # Assert that the key is randomly generated
        self.assertNotEqual(key, key2)


if __name__ == '__main__':
    unittest.main()
