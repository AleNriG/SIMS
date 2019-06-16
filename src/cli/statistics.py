from typing import Generator
from typing import List
from typing import Tuple

import cmd2
import tableformatter as tf
from lib import data
from lib.math import statistics


class Statistics(cmd2.Cmd):

    """Window for calling statistics calculation"""

    HEADER = ["Column", "Range", "Mean", "Std"]

    def __init__(self, datafile: data.Data) -> None:
        """TODO: to be defined1.

        Parameters
        ----------
        datafile : TODO

        """
        cmd2.Cmd.__init__(self)

        self._datafile = datafile

        column: str = self.select(
            self._datafile.ions, "Select column for statistics calculation: "
        )

        rng = self._set_range(column)
        mean, std = self._calculate(self._datafile.points[column])
        formatted_mean, formatted_std = self._format(mean, std)
        row = [(column, rng, formatted_mean, formatted_std)]

        table = self._create_table(Statistics.HEADER, row)
        self.poutput(table)

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

    def _format(self, *args: float) -> Generator[str, None, None]:
        """Format float values to the nice output

        Parameters
        ----------
        args : TODO

        Returns
        -------
        TODO

        """
        return (f"{arg:.2e}" for arg in args)

    def _set_range(self, column: str) -> str:
        """TODO: Docstring for _set_range.
        Returns
        -------
        TODO

        """
        # TODO: manual input range for statistics
        rng_end = len(self._datafile.points[column]) - 1  # due to count from 0
        return f"0:{rng_end}"

    def _create_table(
        self, columns: List[str], row: List[Tuple[str, str, str, str]]
    ) -> str:
        """Create a table formatted output.

        Parameters
        ----------
        columns : TODO
        row : TODO

        Returns
        -------
        TODO

        """
        table = tf.generate_table(row, columns)
        return table
