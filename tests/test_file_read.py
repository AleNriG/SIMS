from src.modules import file_read


with open("tests/testfile.dp_rpc_asc", "r") as file:
    raw_data = []
    for line in file.read().splitlines():
        raw_data.append(line)
start = raw_data.index("*** DATA START ***") + 3
bad_header = raw_data[start]


def test_find_file_name():
    assert file_read._find_file_name(raw_data) == "ZLN170_2-6_neg"


def test_reshape_ion_string():
    assert file_read._reshape_ion_string(bad_header) == ["Time", "28Si", "31P", "75As"]
