# В этом классе содержатся необходимые константы

DATA_BASE_PATH = '../data/twotwo.sqlite'
AREA = 'area'
TITLE = 'title'
LOGIN = 'login'
PASSWORD = 'password'
ITEM = 'item'
NAME = 'name'
COUNT = 'count'
BARCODE = 'barcode'
OWNER_ID = 'owner_id'
PRICE = 'price'
ID = 'id'
NOT_STATED = 'NOT_STATED'
LOGIN_NOT_FOUND_TEXT = 'Введённого вами логина не существует. ' \
                       'Проверьте корректность логина или зарегистрируйтесь'
PASSWORD_NOT_CORRECT_TEXT = 'Пароль, который вы ввели неправильный. ' \
                            'Возможно, вы забыли сменить раскладку' \
                            ' клавиатуры или случайно ввели неверные символы.'
ENCODING_TYPE = 'utf-8'
NAME_FIELD = 'Название'
PRICE_FIELD = 'Цена'
COUNT_FIELD = 'В наличии'
BARCODE_FIELD = 'Штрих-код'
FIELDS = [NAME_FIELD, PRICE_FIELD, COUNT_FIELD, BARCODE_FIELD]
COLUMN_COUNT = len(FIELDS)

