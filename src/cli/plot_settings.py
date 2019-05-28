from modules import data
from modules import selection_menu


class PlotSetup(selection_menu.SelectionMenu):

    """ Plot Settings """

    def __init__(self, datafile: data.Data):
        self._datafile = datafile
        self.programs = [self._set_x]

        selection_menu.SelectionMenu.__init__(self, self.__doc__)
        self._selection_menu_loop(self.programs)

    def _set_x(self):
        """Set X"""
        x = self.select(["Time", "Depth"])
        self._datafile.x = x
