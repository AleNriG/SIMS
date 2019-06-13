from typing import List
from typing import Tuple

import pandas as pd

from .. import data


def asc(filename: str) -> data.Data:
    """Reader for raw data from CAMECA IMS-7f.

    :filename: file to read
    :returns: data object, containing name, points and etc

    """
    with open(filename, "r") as file:
        raw_data = []
        for line in file.read().splitlines():
            raw_data.append(line)
    name = _find_file_name(raw_data)
    bad_header, bad_points = _cut_header_and_points(raw_data)
    header = _reshape_ion_string(bad_header)
    points = _reshape_points(bad_points)
    points = pd.DataFrame(points, columns=header)
    return data.Data(name=name, points=points)


def _find_file_name(raw_data: List[str]) -> str:
    """Find filename, writen inside file itself.

    :raw_text: raw opened data
    :returns: filename

    """
    raw_name_string = raw_data[2]
    name = raw_name_string.split()[-1]
    return name.split(".")[0]


def _cut_header_and_points(raw_data: List[str]) -> Tuple[str, List[str]]:
    """Cut ion names and datapoints from opened file.

    :raw_data: raw opened data
    :returns: header string, points

    """
    start_line = raw_data.index("*** DATA START ***") + 3
    end_line = raw_data.index("*** DATA END ***") - 1
    header = raw_data[start_line]
    points = raw_data[start_line + 2 : end_line]
    return header, points


def _reshape_ion_string(bad_header: str) -> List[str]:
    """Create list of columns for pandas.DataFrame.

    :header: string with ion names
    :returns: list of columns

    """
    header = [ion.replace(" ", "") for ion in filter(None, bad_header.split("\t"))]
    header.insert(0, "Time")
    return header


def _reshape_points(points: List[str]) -> List[List[float]]:
    """Reshape strings with points to float, remove unnecessary points

    :points: strings with data needed
    :returns: array for future pandas.DataFrame

    """
    grid, data = [], []
    for line in points:
        x, *y = map(float, line.split())
        # delete remain time columns
        y = y[0::2]
        grid.append(x)
        data.append(y)

    # insert time column into array
    for i, j in enumerate(grid):
        data[i].insert(0, grid[i])
    return data
