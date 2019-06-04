import os
import random

import pytest
from pytest import list_of

from src.modules import concentration
from src.modules import file_read

TEST_DATAFILE = file_read.asc(
    os.path.join(os.path.dirname(__file__), "files/full_file.dp_rpc_asc")
)


class TestConcentration:
    @pytest.mark.parametrize(
        "impurity, matrix, ia, expected_element",
        [
            ("75As", "28Si", None, "As"),
            ("31P", "28Si", None, "P"),
            ("31P", "28Si", 100, "As"),
            ("75As", "28Si", 100, "P"),
        ],
    )
    def test_set_arguments_and_calculate(self, impurity, matrix, ia, expected_element):
        element, result = concentration.set_arguments_and_calculate(
            TEST_DATAFILE, impurity, matrix, ia
        )
        assert expected_element == element
        assert result == concentration.calculate(
            impurity, ia, matrix, rsf=random.uniform(1e15, 1e25)
        )

    @pytest.mark.randomize(
        impurities=list_of(float, items=100), matrix=list_of(float, items=100)
    )
    def test_calculate(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        assert concentration.calculate(impurities, ia, matrix, rsf) == [
            i / ia / 100 / m * rsf for i, m in zip(impurities, matrix)
        ]

    @pytest.mark.randomize(
        impurities=list_of(float, items=random.randint(1, 100)),
        matrix=list_of(float, items=random.randint(101, 200)),
    )
    def test_list_len(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        with pytest.raises(AssertionError):
            concentration.calculate(impurities, ia, matrix, rsf)
