import pytest
import csv
import os

from src.modules import db


test_database = os.path.join(os.path.dirname(__file__), "files/test_ions_db.csv")


def read_test_db(filepath):
    ions = []
    mass = []
    with open(filepath, 'r') as file:
        for line in csv.reader(file):
            x, y = line
            ions.append(x)
            mass.append(y)
    return ions, mass


ions, mass = read_test_db(test_database)


class TestGetIA:

    @pytest.mark.parametrize(
        "key, expected",
        [(i, j) for i, j in zip(ions, mass)]
    )
    def test_get_ia(self, key, expected):
        db.get_ia(key) == expected
