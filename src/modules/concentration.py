from typing import List


def calculate(
    impurity: List[float], ia: float, matrix: List[float], rsf: float
) -> List[float]:
    """Calculate concentration of element

    Parameters
    ----------
    impurity : list of points of impurity ion impulses/sec
    ia : isotopic abundance of the impurity
    matrix : list of points of matrix ion impulses/sec
    rsf : Relative Sensitivity Factor for the impurity in the matrix

    Returns
    -------
    List of points of element atomic concentration [cm^{-3}]

    """
    assert len(impurity) == len(
        matrix
    ), "Impurity and matrix lists must be the same length!"
    return [i / ia / m * rsf for i, m in zip(impurity, matrix)]
