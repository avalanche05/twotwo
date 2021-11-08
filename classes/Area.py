import Constant


class Area:
    def __init__(self, title, login, password, area_id=-1):
        self.values_name = f'{Constant.TITLE}, {Constant.LOGIN}, {Constant.PASSWORD}'
        self.title = title
        self.login = login
        self.password = password
        self.id = area_id

    def get_values(self) -> str:
        return ', '.join(map(lambda x: f'"{x}"', (self.title, self.login, self.password)))
