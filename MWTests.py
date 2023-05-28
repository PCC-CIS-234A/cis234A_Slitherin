# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        These are test cases for Database and WebUI key gen
# Sources:          	Project Specifications
# *****************************************************************************
import unittest
from Database import Database
from WebUI import WebUI


class TestDB(unittest.TestCase):
    """This class tests various methods in the Database class"""

    def test_connection(self):
        """Test the database connection"""

        Database.connect()
        assert Database.get_connection() is not None

    def test_build_template_list(self):
        """Test the template list builder"""

        template_list = Database.build_template_list()
        assert template_list is not None

    def test_build_email_list(self):
        """Test the email list builder"""

        email_list = Database.build_email_list()
        assert email_list is not None


class TestKey(unittest.TestCase):
    """This class tests key generation methods in the UI class"""

    def test_generate_key(self):
        """Test UI key generation"""

        # Call the generate_key method
        key = WebUI.generate_key()

        # Assert that the key is not None
        self.assertIsNotNone(key)

    def test_key_random(self):
        """Test that the key is random"""

        # Generate two keys
        key = WebUI.generate_key()
        key2 = WebUI.generate_key()

        # Assert that the key is randomly generated
        self.assertNotEqual(key, key2)


if __name__ == '__main__':
    unittest.main()
