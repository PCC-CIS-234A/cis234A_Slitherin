from Database import Database


class AddDB:
    def __init__(self, name, subject, message):
        self.name = name
        self.subject = subject
        self.message = message

    @staticmethod
    def add_to_db(name, subject, message):
        Database.create_template(name, subject, message)
