import sqlite3
import Constant
from classes.Area import Area
from classes.Item import Item
from exceptions.PasswordException import LoginNotFoundException, PasswordNotCorrect
from helpers.PasswordHelper import *


def add_area(area: Area) -> None:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
    INSERT INTO {Constant.AREA}({area.values_name})
     VALUES({area.get_values()}) 
    """

    cursor.execute(request)
    connection.commit()
    connection.close()


def get_area(login: str, password: str) -> Area:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
            SELECT {Constant.TITLE}, {Constant.PASSWORD}, {Constant.ID} FROM {Constant.AREA}
            WHERE {Constant.LOGIN} = "{login}" 
            """

    result = cursor.execute(request).fetchone()

    if not result:
        raise LoginNotFoundException

    title, hashed_password, area_id = result

    if not check_match(hashed_password, password):
        raise PasswordNotCorrect
    connection.close()
    result_area = Area(title, login, hashed_password, area_id)
    return result_area


def add_item(item: Item) -> None:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
        INSERT INTO {Constant.ITEM}({item.values_name})
         VALUES({item.get_values()}) 
        """

    cursor.execute(request)
    connection.commit()
    connection.close()


def get_items(area_id: int) -> list:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
                SELECT {Constant.NAME}, {Constant.COUNT}, {Constant.BARCODE},
                {Constant.OWNER_ID}, {Constant.PRICE}
                 FROM {Constant.ITEM}
                WHERE {Constant.OWNER_ID} = "{area_id}" 
                """

    result = cursor.execute(request).fetchall()

    response = list(map(lambda raw: Item(*raw), result))
    connection.close()
    return response
