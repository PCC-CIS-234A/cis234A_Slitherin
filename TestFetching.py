import unittest
from datetime import datetime
from Database import Database


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_fetch_data_single_date(self):
        self.db.connect()

        date = datetime(2022, 12, 31)

        result = self.db.fetch_data(start_date=date, end_date=date)
        self.assertIsNotNone(result)
        """Perform the data fetching, 
        And Assert that the result is not empty """

    def test_fetch_data_date_range(self):
        self.db.connect()

        start_date = datetime(2022, 12, 31)
        end_date = datetime(2023, 1, 1)

        result = self.db.fetch_data(start_date=start_date, end_date=end_date)
        self.assertIsNotNone(result)
        """Start/end date for the data fetching, 
        And Assert that the result is not empty """

    def test_fetch_data_invalid_date(self):
        self.db.connect()

        invalid_date = datetime(2023, 2, 1)

        result = self.db.fetch_data(start_date=invalid_date, end_date=invalid_date)
        self.assertEqual(result, [])
        """An invalid date for fetching data, 
        And Assert that the result is an empty list """

    def test_fetch_data_no_connection(self):
        self.db.__connection = None

        start_date = datetime(2022, 12, 31)
        end_date = datetime(2022, 12, 31)

        result = self.db.fetch_data(start_date=start_date, end_date=end_date)
        self.assertEqual(result, [])
        """Perform the data fetching, 
        And Assert that the result is None, no database connection) """

    def test_fetch_data_empty_result(self):
        self.db.connect()

        start_date = datetime(2023, 2, 1)
        end_date = datetime(2023, 2, 2)

        result = self.db.fetch_data(start_date=start_date, end_date=end_date)
        self.assertEqual(result, [])
        """Perform the data fetching, 
        And Assert that the result is an empty list """


if __name__ == '__main__':
    unittest.main()
