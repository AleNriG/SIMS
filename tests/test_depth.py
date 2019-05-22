import pytest

from src.modules import depth

TIME = [0.3 * i for i in range(101)]


@pytest.mark.randomize(time=pytest.list_of(float), speed=float, positive=True)
def test_homostructure(time, speed):
    assert depth._homostructure(time, speed) == [i * speed for i in time]


@pytest.mark.parametrize(
    "speed, indexes, expected",
    [
        ([1.0, 2.0], [3], 59.4000000000001),
        ([1.0, 2.0], [4], 59.100000000000094),
        ([1.0, 2.0, 3.0], [2, 5], 88.50000000000009),
    ],
)
def test_heterostructure(speed, indexes, expected):
    assert depth._heterostructure(TIME, speed, indexes)[-1] == expected


@pytest.mark.parametrize(
    "speed, indexes, expected", [(2.0, None, 60.0), ([1.0, 2.0], [3], 59.4000000000001)]
)
def test_calculate(speed, indexes, expected):
    assert depth.calculate(TIME, speed, indexes)[-1] == expected


@pytest.mark.parametrize(
    "time, speed, indexes, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "a", None, 20.0),
        ([1.0, 2.0, "a"], 12, ["a", 3], 16.0),
        ([1.0, 2.0, "a"], 12, [3], 24),
    ],
)
def test_calculate_exception(time, speed, indexes, expected):
    with pytest.raises(Exception) as e:
        assert depth.calculate(time, speed, indexes)
    assert str(e.value) == "Invalid variables"
