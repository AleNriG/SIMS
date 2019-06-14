from typing import List
from typing import Tuple

import cmd2
from lib import data
from lib.math import statistics


class Statistics(cmd2.Cmd):

    """Window for calling statistics calculation"""

    def __init__(self, datafile: data.Data):
        """TODO: to be defined1.

        Parameters
        ----------
        datafile : TODO

        """
        cmd2.Cmd.__init__(self)

        self._datafile = datafile

        column = self.select(
            self._datafile.ions, "Select column for statistics calculation: "
        )
        mean, std = self._calculate(self._datafile.points[column])
        self.poutput(f"mean = {mean}")
        self.poutput(f"std = {std}")

    def _calculate(self, values: List[float]) -> Tuple[float, float]:
        """TODO: Docstring for _calculate.

        Parameters
        ----------
        values : TODO

        Returns
        -------
        TODO

        """
        result = statistics.mean(values), statistics.std(values)
        return result
