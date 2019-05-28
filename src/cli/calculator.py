from modules import manual_input
from modules import minor
from modules import selection_menu


class Calculator(selection_menu.SelectionMenu):

    """Helpful Calculator"""

    def __init__(self):
        title = self.__doc__
        self.programs = [self._rsf, self._hmr]

        selection_menu.SelectionMenu.__init__(self, title=title)
        self._selection_menu_loop(self.programs)

    def _rsf(self):
        """Calculate RSF"""
        dose = manual_input.read_float(message="Input dose: ")
        integer = manual_input.read_float(message="Input integration result: ")
        try:
            result = minor.rsf(dose=dose, integer=integer)
            self.poutput(f"RSF = {result:.2e}")
        except ZeroDivisionError as e:
            self.perror(f"{e}")

    def _hmr(self):
        """Calculate HMR"""
        mass_1 = manual_input.read_eval(message="Input expression for the first mass: ")
        mass_2 = manual_input.read_eval(
            message="Input expression for the second mass: "
        )
        try:
            result = minor.hmr(mass_1, mass_2)
            self.poutput(f"HMR = {int(result)}")
        except ZeroDivisionError as e:
            self.perror(f"{e}")
