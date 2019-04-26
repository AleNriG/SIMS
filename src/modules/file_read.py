#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: read.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""
from typing import List, Tuple
from modules import data
import pandas as pd


def asc(filename: str) -> data.Data:
    """Reader for raw data from CAMECA IMS-7f

    :filename: TODO
    :returns: TODO

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
    """TODO: Docstring for _find_file_name.

    :raw_text: TODO
    :returns: TODO

    """
    raw_name_string = raw_data[2]
    name = raw_name_string.split()[-1]
    return name.split(".")[0]


def _cut_header_and_points(raw_data: List[str]) -> Tuple[str, List[str]]:
    """TODO: Docstring for _cut_points.

    :raw_data: TODO
    :returns: TODO

    """
    start_line = raw_data.index("*** DATA START ***") + 3
    end_line = raw_data.index("*** DATA END ***") - 1
    header = raw_data[start_line]
    points = raw_data[start_line + 2 : end_line]
    return header, points


def _reshape_ion_string(bad_header: str) -> List[str]:
    """TODO: Docstring for _parse_ion_names.

    :header: TODO
    :returns: TODO

    """
    header = [ion.replace(" ", "") for ion in filter(None, bad_header.split("\t"))]
    header.insert(0, "Time")
    return header


def _reshape_points(points: List[str]) -> List[List[float]]:
    """TODO: Docstring for _reshape_points.

    :points: TODO
    :returns: TODO

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
