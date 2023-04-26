# *****************************************************************************
# Author:           	Slitherin' - Mike Winebarger
# Date:		            April 2023
# Description:	        This is a temporary template class for testing
# Sources:          	Project Specifications
# *****************************************************************************

class Template:
    def __init__(self, name, subject, text):
        self.__name = name
        self.__subject = subject
        self.__text = text

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_subject(self):
        return self.__subject

    def get_text(self):
        return self.__text

    def get_key(self):
        return self.__name.lower()

    @staticmethod
    def build_list():
        temp1 = Template(
            'Default',
            'Food Available!',
            'Food is now available at Panther Pantry!'
        )

        temp2 = Template(
            'Perishable',
            'Perishable Food Available!',
            """Perishable food is now available at Panther Pantry!\n
            \nGet it while it\'s good!"""
        )

        temp3 = Template(
            'New Item',
            'New Item Available!',
            """There is a new item available at Panther Pantry!\n
            \nWe now have <BLANK>. Come and get your <BLANK>!"""
        )

        template_list = [temp1, temp2, temp3]

        return template_list
