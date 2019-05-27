from selection_menu import SelectionMenu


class Calculator(SelectionMenu):

    """Helpful Calculator"""

    def __init__(self):
        title = self.__doc__
        SelectionMenu.__init__(self, title=title)

    def mock_1(self):
        pass

    def mock_2(self):
        pass

    def call(self):
        self.commands = ["mock 1", "mock 2"]
        self._selection_menu_loop(self.commands)
