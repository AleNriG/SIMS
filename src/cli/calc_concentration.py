import cmd2
from modules import concentration
from modules import data
from modules import manual_input


class CalculateConcentration(cmd2.Cmd):

    """Docstring for CalculateConcentration. """

    def __init__(self, datafile: data.Data):
        """TODO: to be defined1.

        Parameters
        ----------
        datafile : TODO


        """
        cmd2.Cmd.__init__(self)

        self._datafile = datafile
        self._set_arguments()

    def _set_arguments(self):
        """TODO: Docstring for _set_arguments.
        Returns
        -------
        TODO

        """
        ia = None
        matrix = self.select(self._datafile.ions, "Select matrix: ")
        self._datafile.set_matrix(matrix)
        impurity = self.select(self._datafile.impurities, "Select impurity: ")
        answer = self.select(["Yes", "No"], "Use isotopic abundance from database? ")
        if answer == "No":
            ia = manual_input.read_float(message="Input isotopic abundance: ")
        element, result = concentration.set_arguments_and_calculate(
            self._datafile, impurity, matrix, ia
        )
        self._datafile.points[element] = result
