class Area:
    def __init__(self, title, login, password):
        self.title = title
        self.login = login
        self.password = password

    def get_values(self):
        return ', '.join(map(lambda x: f'"{x}"', (self.title, self.login, self.password)))
