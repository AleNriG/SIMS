import pytest

from src.modules import minor


@pytest.mark.randomize(dose=float, integer=float, positive=True)
def test_minor_rsf(dose, integer):
    assert minor.rsf(dose, integer) == dose / integer * 10 ** 7


@pytest.mark.randomize(mass1=float, mass2=float, positive=True)
def test_minor_hmr(mass1, mass2):
    assert minor.hmr(mass1, mass2) == mass2 / abs(mass1 - mass2)
