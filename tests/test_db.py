import pytest
import csv
import os

from src.modules import db


test_database = os.path.join(os.path.dirname(__file__), "files/test_ions_db.csv")


def read_test_db(filepath):
    ions = []
    mass = []
    with open(filepath, "r") as file:
        for line in csv.reader(file):
            x, y = line
            ions.append(x)
            mass.append(y)
    return ions, mass


IONS, MASS = read_test_db(test_database)

ELEMENTS = (
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "In",
    "Sn",
    "Sb",
    "Te",
    "I",
    "Xe",
    "Cs",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Ho",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "Th",
    "U",
)


class TestDB:
    @pytest.mark.parametrize("key, expected", [(i, j) for i, j in zip(IONS, MASS)])
    def test_get_ia(self, key, expected):
        db.get_ia(key) == expected


def test_strip_ions_names(self):
    result = [db._strip_ion(ion) for ion in IONS]
    result = set(result)
    assert result == ELEMENTS
