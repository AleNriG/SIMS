import cmd2


class SelectionMenu(cmd2.Cmd):

    """Parental class menus using cmd2 select."""

    def __init__(self, title):
        """TODO: to be defined1.

        Parameters
        ----------
        title : menu title


        """
        cmd2.Cmd.__init__(self)

        self._title = title
