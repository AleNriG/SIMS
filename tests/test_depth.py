import pytest

from src.modules import depth


@pytest.mark.randomize(time=pytest.list_of(float), speed=float, positive=True)
def test_homostructure(time, speed):
    assert depth.homostructure(time, speed) == [i * speed for i in time]


@pytest.mark.parametrize(
    "speed, indexes, expected",
    [
        ([1.0, 2.0], [3], 16.0),
        ([1.0, 2.0], [4], 20.0),
        ([1.0, 2.0, 3.0], [1, 3, 5], 22.0),
    ],
)
def test_heterostructure(speed, indexes, expected):
    time = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    assert depth.heterostructure(time, speed, indexes)[-1] == expected
