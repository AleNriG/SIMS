import cmd2

from ..lib import data


class DepthCalculation(cmd2.Cmd):

    """Depth calculation window"""

    def __init__(self, datafile: data.Data):
        cmd2.Cmd.__init__(self)

        self._datafile = datafile
