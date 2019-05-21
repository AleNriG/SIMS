import pytest

from src.modules import db


class TestGetIA:

    @pytest.mark.parametrize(
        "key, expected",
        [('1H', 99.985), ('24Mg', 78.99), ('27Al', 100.0)]
    )
    def test_get_ia(self, key, expected):
        db.get_ia(key) == expected
