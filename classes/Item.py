import Constant


class Item:
    def __init__(self, name: str, count: int, barcode: str, owner_id: int, price: float):
        self.values_name = f'{Constant.NAME}, {Constant.COUNT},' \
                           f' {Constant.BARCODE}, {Constant.OWNER_ID}, ' \
                           f'{Constant.PRICE}'
        self.id = -1
        self.name = name
        self.count = count
        self.barcode = barcode
        self.owner_id = owner_id
        self.price = price

    def get_values(self) -> str:
        return ', '.join(map(lambda x: f'"{x}"',
                             (self.name, self.count, self.barcode, self.owner_id, self.price)))
