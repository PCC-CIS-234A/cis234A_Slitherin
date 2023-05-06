from Database import Database


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
        """This method builds a list of templates"""

        return Database.build_template_list()
