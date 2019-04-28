import pytest

from src.modules import file_read


def reader(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line)
    return data


with open("tests/testfiles/full_file.dp_rpc_asc", "r") as file:
    raw_data = []
    for line in file.read().splitlines():
        raw_data.append(line)
start = raw_data.index("*** DATA START ***") + 3
bad_header = raw_data[start]


def test_find_file_name():
    assert file_read._find_file_name(raw_data) == "ZLN170_2-6_neg"


@pytest.mark.parametrize("given", reader("tests/testfiles/headers"))
def test_reshape_ion_string(given):
    print(given)
    expected = ["Time", "28Si", "31P", "75As"]
    assert file_read._reshape_ion_string(given) == expected
