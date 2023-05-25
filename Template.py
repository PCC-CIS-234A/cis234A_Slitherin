# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This is a class definition for templates
# Sources:          	Project Specifications
# *****************************************************************************
from Database import Database


class Template:
    def __init__(self, name, subject, message):
        self.__name = name
        self.__subject = subject
        self.__message = message

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message

    def get_key(self):
        return self.__name.lower()

    @staticmethod
    def build_list():
        """This method builds a list of templates"""

        return Database.build_template_list()
