from Database import Database

class AddDB:
    def __init__(self, subject, message, sender_id, time_sent, count):
        self.subject = subject
        self.message = message
        self.sender_id = sender_id
        self.time_sent = time_sent
        self.send_count = count

    @staticmethod
    def add_to_db(name, subject, message):

        Database.create_template(name, subject, message)