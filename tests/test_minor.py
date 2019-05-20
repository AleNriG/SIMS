import pytest
import random
from pytest import list_of

from src.modules import minor

@pytest.mark.randomize(dose=float, integer=float, positive=True)
def test_minor_rsf(dose, integer):
    assert minor.rsf(dose, integer) == dose / integer * 10 ** 7


@pytest.mark.randomize(mass1=float, mass2=float, positive=True)
def test_minor_hmr(mass1, mass2):
    assert minor.hmr(mass1, mass2) == mass2 / abs(mass1 - mass2)


class TestConcentration:
    @pytest.mark.randomize(
        impurities=list_of(float, items=100),
        matrix=list_of(float, items=100),
    )
    def test_random(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        assert (
            minor.concentration(impurities, ia, matrix, rsf) ==
            [i / ia / m * rsf for i, m in zip(impurities, matrix)]
        )

    @pytest.mark.randomize(
        impurities=list_of(float, items=random.randint(1, 100)),
        matrix=list_of(float, items=random.randint(101, 200)),
    )
    def test_list_len(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        with pytest.raises(AssertionError):
            minor.concentration(impurities, ia, matrix, rsf)
