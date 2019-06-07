import cmd2

from ..lib import data
from ..lib.io import manual_input


class DepthCalculation(cmd2.Cmd):

    """Depth calculation window"""

    def __init__(self, datafile: data.Data):
        super().__init__(self)

        self._datafile = datafile

    def _set_layers_value(self) -> int:
        """Input the number of layers in structure

        Returns
        -------
        Int number of layers in structure

        """
        layers = manual_input.read_int(message="Input layers number: ")
        while layers <= 0:
            self.poutput("Layers value must be positive!")
            layers = manual_input.read_int(message="Input layers number: ")
        return layers

    def _determine_structure(self, layers: int):
        if layers == 1:
            self._set_args_to_homostructure()
        else:
            self._set_args_to_heterostructure()

    def _set_args_to_homostructure(self):
        """TODO: Docstring for _set_args_to_homostructure.
        Returns
        -------
        TODO

        """
        pass

    def _set_args_to_heterostructure(self):
        """TODO: Docstring for _set_args_to_heterostructure.
        Returns
        -------
        TODO

        """
        pass
