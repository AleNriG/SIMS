from . import selection_menu


class OutputFormat(selection_menu.SelectionMenu):

    """Saving file format"""

    def __init__(self):
        """TODO: to be defined1. """
        title = self.__doc__
        self.programs = [self._csv]

        selection_menu.SelectionMenu.__init__(self, title=title)
        self._selection_menu_loop(self.programs)

    def _csv(self):
        """Save to CSV"""
        pass
