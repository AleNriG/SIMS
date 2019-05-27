from typing import Callable
from typing import List

import cmd2


class SelectionMenu(cmd2.Cmd):

    """Parental class menus using cmd2 select."""

    def __init__(self, title: str) -> None:
        """Initialize selection menu class.

        Parameters
        ----------
        title : menu title

        """
        cmd2.Cmd.__init__(self)

        self._title = title.center(30, "~")

    def _selection_menu_loop(self, commands: List[str], programs: List[Callable]):
        """Start selection loop.

        Parameters
        ----------
        commands : functions docs
        programs : functions to call

        Returns
        -------
        Call of chosen program

        """
        commands.append("Back")
        while True:
            self.poutput(self._title)
            chosen_command = self.select(commands)
            if chosen_command == "Back":
                break
            self.chosen_program = commands.index(chosen_command)
            programs[self.chosen_program]()
