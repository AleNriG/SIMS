from typing import List
from typing import Tuple

from . import data
from . import db
from . import manual_input


def set_arguments_and_calculate(
    datafile: data.Data, impurity: str, matrix: str
) -> Tuple[str, List[float]]:
    """Calculate atomic concentration of impurity.
    API for manual parameters setting.

    Parameters
    ----------
    impurity : name of the impurity
    matrix : name of the matrix

    Returns
    -------
    List of points of element atomic concentration [cm^{-3}]

    """
    ia = db.get_ia(impurity)
    element = db._strip_ion(impurity)

    rsf = manual_input.read_float(message="Input RSF: ")
    concentration = calculate(
        datafile.points[impurity], ia, datafile.points[matrix], rsf
    )
    return element, concentration


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
