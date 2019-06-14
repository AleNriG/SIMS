import os

import numpy

from src.lib.io import file_read
from src.lib.math import statistics

TEST_INPUT_FILE = os.path.join(os.path.dirname(__file__), "files/full_file.dp_rpc_asc")
TEST_DATA = file_read.asc(TEST_INPUT_FILE)


class TestStatistics:

    """Tests for statistics module"""

    def test_mean(self):
        result = []
        for column in TEST_DATA.points:
            result.append(statistics.mean(TEST_DATA.points[column]))
        expected = TEST_DATA.points.mean()
        expected = expected.get_values()

        # Because of difference in a looong after the dot (46617.96228563013 and
        # 46617.96228563009), lets round them

        rounded_result = [round(i, 2) for i in result]
        rounded_expected = [round(i, 2) for i in expected.tolist()]

        assert rounded_result == rounded_expected

    def test_std(self):
        """Change std expected calculation due to severe difference
        between nympy.std and pandas.std
        """
        result, expected = [], []
        for column in TEST_DATA.points:
            result.append(statistics.std(TEST_DATA.points[column]))
            expected.append(numpy.std(TEST_DATA.points[column]))

        # Same thing here

        rounded_result = [round(i, 2) for i in result]
        rounded_expected = [round(i, 2) for i in expected]

        assert rounded_result == rounded_expected
