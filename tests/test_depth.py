import pytest

from src.modules import depth


@pytest.mark.randomize(time=pytest.list_of(float), speed=float, positive=True)
def test_homostructure(time, speed):
    assert depth.homostructure(time, speed) == [i * speed for i in time]
