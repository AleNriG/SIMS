from typing import List
from typing import Optional

import cmd2


class SelectionMenu(cmd2.Cmd):

    """Parental class menus using cmd2 select."""

    def __init__(self, title: str) -> None:
        """TODO: to be defined1.

        Parameters
        ----------
        title : menu title

        """
        cmd2.Cmd.__init__(self)

        self._title = title.center(30, "~")

    def _selection_menu_loop(self, commands: List[str]) -> Optional[int]:
        """TODO: Docstring for _selection_menu_loop.

        Parameters
        ----------
        commands : TODO

        Returns
        -------
        TODO

        """
        pass
