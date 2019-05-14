import pytest

from src.modules import depth


@pytest.mark.randomize(time=pytest.list_of(float), speed=float, positive=True)
def test_homostructure(time, speed):
    assert depth._homostructure(time, speed) == [i * speed for i in time]


@pytest.mark.parametrize(
    "speed, indexes, expected",
    [([1.0, 2.0], [3], 18.5), ([1.0, 2.0], [4], 18.0), ([1.0, 2.0, 3.0], [2, 5], 26.5)],
)
def test_heterostructure(speed, indexes, expected):
    time = [
        0.5,
        1.0,
        1.5,
        2.0,
        2.5,
        3.0,
        3.5,
        4.0,
        4.5,
        5.0,
        5.5,
        6.0,
        6.5,
        7.0,
        7.5,
        8.0,
        8.5,
        9.0,
        9.5,
        10.0,
    ]
    assert depth._heterostructure(time, speed, indexes)[-1] == expected


@pytest.mark.parametrize(
    "speed, indexes, expected", [(2.0, None, 20.0), ([1.0, 2.0], [3], 17.0)]
)
def test_calculate(speed, indexes, expected):
    time = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    assert depth.calculate(time, speed, indexes)[-1] == expected


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
