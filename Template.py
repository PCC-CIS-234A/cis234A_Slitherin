# *****************************************************************************
# Author:           	Slitherin'
# Date:		            April 2023
# Description:	        This is a class definition for templates
# Sources:          	Project Specifications
# class AddDB:
# def __init__(self, name, subject, message):
# self.name = name
# self.subject = subject
# self.message = message
# *****************************************************************************
from flask import flash

from Database import Database


class Template:
    def __init__(self, name, subject, message, tags):
        self.__name = name
        self.__subject = subject
        self.__message = message
        self.__tags = tags

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message

    def get_tags(self):
        return self.__tags

    def get_key(self):
        return self.__name.lower()

    @staticmethod
    def build_list():
        """This method builds a list of templates"""

        return Database.build_template_list()

    @staticmethod
    def add_to_db(name, subject, message):
        Database.create_template(name, subject, message)

    @staticmethod
    def update_to_db(name, subject, message):
        Database.update_template(name, subject, message)

    @staticmethod
    def validate_template_name(name):
        if '' in name:
            flash("Template must have name.", category='error')
            return True

    @staticmethod
    def validate_template_subject(subject):
        if '' in subject:
            flash("Template must have subject.", category='error')
            return True

    @staticmethod
    def validate_template_message(message):
        if '' in message:
            flash("Template must have a message.", category='error')
            return True
