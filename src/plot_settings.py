from modules import selection_menu


class PlotSetup(selection_menu.SelectionMenu):

    """ Plot Settings """

    def __init__(self):
        self.programs = [self._set_x]

        selection_menu.SelectionMenu.__init__(self, self.__doc__)
        self._selection_menu_loop(self.programs)

    def _set_x(self):
        """Set X"""
        pass
