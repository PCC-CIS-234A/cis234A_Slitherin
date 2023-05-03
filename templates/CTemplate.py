class CTemplate:
    def __init__(self, name, subject, message):
        self.name = name
        self.subject = subject
        self.message = message

    @staticmethod
    def build_list():
        temp1 = CTemplate(
            'Default',
            'Food Available!',
            'Food is now available at Panther Pantry!\n'
        )

        temp2 = CTemplate(
            'Perishable',
            'Perishable Food Available!',
            'Perishable food is now available at Panther Pantry!\n'
            '\nGet it while it\'s good!'
        )

        temp3 = CTemplate(
            name='New Item',
            subject='New Item Available!',
            message='There is a new item available at Panther Pantry!\n'
                    '\nWe now have <BLANK>. Come and get your <BLANK>!'
        )

        template_list = [temp1, temp2, temp3]

        return template_list

    def get_name(self):
        return self.name
