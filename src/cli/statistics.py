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
        cmd2.Cmd.__init__(self)

        self._datafile = datafile

        self._exec()

    def _exec(self):
        """Execute statistics calculation

        Returns
        -------
        Prints table with selected column, range of calculation, mean and std.

        """
        column = self._select_column()

        rng_start, rng_end = self._set_range(column)
        str_rng = self._format_range(rng_start, rng_end)

        # +1 to include last point in calculations
        mean, std = self._calculate(
            self._datafile.points[column][rng_start : rng_end + 1]
        )

        row = [(column, str_rng, mean, std)]

        table = self._create_table(Statistics.HEADER, row)
        self.poutput(table)

    def _select_column(self) -> str:
        """Select column in data for statistics calculation

        Returns
        -------
        String of selected column name.

        """
        column: str = self.select(
            list(self._datafile.points.columns),
            "Select column for statistics calculation: ",
        )
        return column

    def _set_range(self, column: str) -> Tuple[int, int]:
        """Set range for statistics calculations

        Returns
        -------
        Column indexes of the beginning and the ending of statistics calculations.

        """
        str_range = input("Input range (a:b) [default full list]: ")

        if not str_range:
            rng_start = 0
            rng_end = len(self._datafile.points[column]) - 1  # due to count from 0
            return rng_start, rng_end

        rng_start, rng_end = self._split_str(str_range)
        return rng_start, rng_end

    def _format_range(self, rng_start: int, rng_end: int) -> str:
        """Format range values to a string with type 'start:end'

        Parameters
        ----------
        rng_start : first range point
        rng_end : last range point

        Returns
        -------
        String formatted to 'start:end'

        """
        return f"{rng_start}:{rng_end}"

    def _split_str(self, string: str) -> Generator[int, None, None]:
        return (int(i) for i in string.split(":"))

    def _calculate(self, values: List[float]) -> Tuple[str, str]:
        """Calculate mean and std

        Parameters
        ----------
        values : list of values of selected column in selected range

        Returns
        -------
        Mean and std

        """
        raw_mean, raw_std = statistics.mean(values), statistics.std(values)
        mean, std = self._format_calculations(raw_mean, raw_std)
        return mean, std

    def _format_calculations(self, *args: float) -> Generator[str, None, None]:
        """Format float values to the nice output

        Parameters
        ----------
        args : values after statistics calculations

        Returns
        -------
        Rounded to two numbers after dot in scientific style strings

        """
        return (f"{arg:.2e}" for arg in args)

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
