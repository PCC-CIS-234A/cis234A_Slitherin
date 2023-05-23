import unittest

import unittest

from Template import Template


class TestTemplate(unittest.TestCase):
    def test_get_name(self):
        name = 1
        subject = 2
        test = 3
        key = 4

    template = Template(name, subject, text, key)

    self.assertEqual(name, template.get_name())
    self.assertEqual(subject, template.get_subject())
    self.assertEqual(text, template.get_text())
    self.assertEqual(key, template.get_key())
