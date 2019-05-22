from typing import List


def hmr(mass_1: float, mass_2: float) -> float:
    return mass_2 / abs(mass_1 - mass_2)


def rsf(dose: float, integer: float) -> float:
    return dose / integer * 10 ** 7


def concentration(
    impurity: List[float], ia: float, matrix: List[float], rsf: float
) -> List[float]:
    assert len(impurity) == len(
        matrix
    ), "Impurity and matrix lists must be the same lenght!"
    return [i / ia / m * rsf for i, m in zip(impurity, matrix)]
