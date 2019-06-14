from typing import Dict
from typing import List
from typing import Tuple

import cmd2
from lib import data
from lib.math import statistics


class Statistics(cmd2.Cmd):

    """Window for calling statistics calculation"""

    def __init__(self, datafile: data.Data) -> None:
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
        self._str({"mean": mean, "std": std})

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

    def _str(self, *args: Dict[str, float]):
        """Print all calculated args

        Parameters
        ----------
        args* : TODO

        Returns
        -------
        TODO

        """
        for arg in args:
            for key, value in arg.items():
                print(f"{key} = {round(value, 2):.2e}")
