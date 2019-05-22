import sqlite3
import os

database = os.path.join(os.path.dirname(__file__), "../db/ia.db3")


def get_ia(key: str) -> float:
    """TODO: Docstring for get_value.

    :key: TODO
    :returns: TODO

    """
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()

        request = f"SELECT abundance FROM abundance WHERE species IS '{key}'"
        cursor.execute(request)
        result = cursor.fetchone()[0]
    return result
