import unittest
from Database import Database
from WebUI import WebUI


class TestDB(unittest.TestCase):
    """This method tests various methods in the Database class
    Numeric values should be changed to reflect database changes"""

    def test_connection(self):
        """Test the database connection"""

        Database.connect()
        assert Database.__connection is not None

    def test_build_template_list(self):
        """Test the template list - Value should be edited as the size changes
        I know that this is not a good test, but there aren't many
        methods that I wrote that are testable"""

        # Assuming there are 5 templates in the database
        expected_templates = 5
        template_list = Database.build_template_list()
        assert len(template_list) == expected_templates

    def test_build_email_list(self):
        """Test the template list - Value should be edited as the size changes
        I know that this is not a good test, but there aren't many
        methods that I wrote that are testable"""

        # Assuming there are 5 subscribers in the database
        expected_subscribers = 5
        email_list = Database.build_email_list()
        assert len(set(email_list)) == expected_subscribers


class TestUI(unittest.TestCase):
    def test_generate_key(self):
        """This method defines tests for the key"""

        # Call the generate_key method
        key = WebUI.generate_key()

        # Assert that the key is not None
        self.assertIsNotNone(key)

        # Assert that the key is randomly generated
        key2 = WebUI.generate_key()
        self.assertNotEqual(key, key2)


if __name__ == '__main__':
    unittest.main()
