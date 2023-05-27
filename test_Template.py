import unittest

import unittest

from Template import Template


class TestTemplate(unittest.TestCase):
    def test_get_name(self):
        name = 1
        subject = 2
        message = 3

        template = Template(name, subject, message)

        self.assertEqual(name, template.get_name())
        self.assertEqual(subject, template.get_subject())
        self.assertEqual(message, template.get_message())

