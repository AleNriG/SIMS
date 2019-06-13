import os

from src.lib.io import file_read


def reader(filename):
    datafile = []
    with open(filename, "r") as file:
        for line in file.read().splitlines():
            datafile.append(line)
    return datafile


NAME = "ZLN170_2-6_neg"
BAD_HEADER = "28Si\t\t\t\t\t31P"
BAD_POINTS = [
    "4.53333E-002\t\t9.40730E+006\t8.93333E-002\t\t1.27277E+005",
    "1.78667E-001\t\t7.83114E+007\t2.06667E-001\t\t2.21947E+005",
    "2.96000E-001\t\t9.50838E+007\t3.24000E-001\t\t2.93436E+005",
]
HEADER = ["Time", "28Si", "31P"]
POINTS = [
    [4.53333e-002, 9.40730e006, 1.27277e005],
    [1.78667e-001, 7.83114e007, 2.21947e005],
    [2.96000e-001, 9.50838e007, 2.93436e005],
]


test_file = os.path.join(os.path.dirname(__file__), "files/simple.dp_rpc_asc")


def test_find_file_name():
    expected = NAME
    assert file_read._find_file_name(reader(test_file)) == expected


def test_cut_header_and_points():
    expected = (BAD_HEADER, BAD_POINTS)
    assert file_read._cut_header_and_points(reader(test_file)) == expected


def test_reshape_ion_string():
    expected = HEADER
    assert file_read._reshape_ion_string(BAD_HEADER) == expected


def test_reshape_points():
    expected = POINTS
    assert file_read._reshape_points(BAD_POINTS) == expected
