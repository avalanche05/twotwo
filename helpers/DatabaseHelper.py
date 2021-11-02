import sqlite3
import Constant
from classes.Area import Area
from exceptions.PasswordException import LoginNotFoundException, PasswordNotCorrect
from helpers.PasswordHelper import *


def add_area_in_db(area: Area) -> None:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
    INSERT INTO area({Constant.TITLE}, {Constant.LOGIN}, {Constant.PASSWORD})
     VALUES({area.get_values()}) 
    """

    cursor.execute(request)
    connection.commit()
    connection.close()


def get_area(login: str, password: str) -> Area:
    connection = sqlite3.connect(Constant.DATA_BASE_PATH)
    cursor = connection.cursor()

    request = f"""
            SELECT {Constant.TITLE}, {Constant.PASSWORD} FROM {Constant.AREA}
            WHERE {Constant.LOGIN} = "{login}" 
            """

    result = cursor.execute(request).fetchone()

    if not result:
        raise LoginNotFoundException

    title, hashed_password = result

    if not check_match(hashed_password, password):
        raise PasswordNotCorrect
    connection.close()
    result_area = Area(title, login, hashed_password)
    return result_area
