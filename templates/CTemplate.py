class Template:
    def __init__(self, name, subject, message):
        self.__name = name
        self.__subject = subject
        self.__message = message

    def __str__(self):
        return self.__name

    def get_key(self):
        return self.__name.lower()

    @staticmethod
    def build_list():
        temp1 = Template(
            'Default',
            'Food Available!',
            'Food is now available at Panther Pantry!\n'
        )

        temp2 = Template(
            'Perishable',
            'Perishable Food Available!',
            'Perishable food is now available at Panther Pantry!\n'
            '\nGet it while it\'s good!'
        )

        temp3 = Template(
            name='New Item',
            subject='New Item Available!',
            text='There is a new item available at Panther Pantry!\n'
            '\nWe now have <BLANK>. Come and get your <BLANK>!'
        )

        template_list = [temp1, temp2, temp3]

        return template_list

    def get_name(self):
        return self.__name