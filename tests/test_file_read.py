from src.modules import file_read


def reader(filename):
    datafile = []
    with open(filename, "r") as file:
        for line in file.read().splitlines():
            datafile.append(line)
    return datafile


file_name = "ZLN170_2-6_neg"
bad_header = "28Si\t\t\t\t\t31P\t\t\t\t\t75As"
bad_points = [
    "4.53333E-002\t\t9.40730E+006\t8.93333E-002\t\t1.27277E+005\t1.29333E-001\t\t6.96442E+003",
    "1.78667E-001\t\t7.83114E+007\t2.06667E-001\t\t2.21947E+005\t2.46667E-001\t\t4.13942E+003",
    "2.96000E-001\t\t9.50838E+007\t3.24000E-001\t\t2.93436E+005\t3.64000E-001\t\t2.71346E+003",
]
header = ["Time", "28Si", "31P", "75As"]
points = [
    [4.53333e-002, 9.40730e006, 1.27277e005, 6.96442e003],
    [1.78667e-001, 7.83114e007, 2.21947e005, 4.13942e003],
    [2.96000e-001, 9.50838e007, 2.93436e005, 2.71346e003],
]


def test_find_file_name():
    expected = file_name
    assert (
        file_read._find_file_name(reader("tests/files/simple.dp_rpc_asc")) == expected
    )


def test_cut_header_and_points():
    expected = (bad_header, bad_points)
    assert (
        file_read._cut_header_and_points(reader("tests/files/simple.dp_rpc_asc"))
        == expected
    )


def test_reshape_ion_string():
    expected = header
    assert file_read._reshape_ion_string(bad_header) == expected


def test_reshape_points():
    expected = points
    assert file_read._reshape_points(bad_points) == expected
