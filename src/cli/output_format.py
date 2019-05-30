from . import selection_menu
from src.modules import data


class OutputFormat(selection_menu.SelectionMenu):

    """Saving file format"""

    def __init__(self, datafile: data.Data, filepath: str):
        """TODO: to be defined1.

        Parameters
        ----------
        datafile : TODO


        """
        self._datafile = datafile
        self._filepath = filepath

        title = self.__doc__
        self.programs = [self._csv]

        selection_menu.SelectionMenu.__init__(self, title=title)
        self._selection_menu_loop(self.programs)

    def _csv(self):
        """Save to CSV"""
        self._datafile.set_output_format(".csv")
