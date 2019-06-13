import os
import sqlite3

DATABASE = os.path.join(os.path.dirname(__file__), "../db/ia.db3")


def _strip_ion(ion: str) -> str:
    symbols = [symbol for symbol in ion if symbol.isalpha()]
    element = "".join(symbols)
    return element


def get_ia(key: str) -> float:
    """TODO: Docstring for get_value.

    :key: TODO
    :returns: TODO

    """
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        request = f"SELECT abundance FROM abundance WHERE species IS '{key}'"
        cursor.execute(request)
        result = cursor.fetchone()[0]
    return result
