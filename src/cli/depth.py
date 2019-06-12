from typing import Any
from typing import List
from typing import Tuple

import cmd2

from ..lib import data
from ..lib.io import manual_input
from ..lib.math import depth


class DepthCalculation(cmd2.Cmd):

    """Depth calculation window"""

    def __init__(self, datafile: data.Data):
        super().__init__(self)

        self._datafile = datafile

        layers = self._set_layers_value()
        speed, indexes = self._determine_structure(layers)
        self._calculate(speed, indexes)

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
            arguments = self._set_args_for_homostructure()
        else:
            arguments = self._set_args_to_heterostructure()
        return arguments

    def _set_args_for_homostructure(self) -> Tuple[float, None]:
        """TODO: Docstring for _set_args_to_homostructure.
        Returns
        -------
        TODO

        """
        self.poutput("Calculating depth for homostructure")
        speed = manual_input.read_float(message="Input speed: ")
        indexes = None
        return speed, indexes

    def _set_args_to_heterostructure(
        self, layers: int
    ) -> Tuple[List[float], List[int]]:
        """TODO: Docstring for _set_args_to_heterostructure.

        Parameters
        ----------
        layers : TODO

        Returns
        -------
        TODO

        """
        self.poutput("Calculating depth for heterostructure")
        speed = self._get_list_of_values(
            layers, values_type="float", message="Input speed of the layer: "
        )
        indexes = self._get_list_of_values(
            layers, values_type="int", message="Input speed of the layer: "
        )
        return speed, indexes

    def _get_list_of_values(
        self, layers: int, values_type: str, message: str
    ) -> List[Any]:
        """Get list of positive and non repetitive values of integers or floats.

        Parameters
        ----------
        layers : TODO
        values_type : TODO
        message : TODO

        Returns
        -------
        TODO

        """
        if values_type == "int":  # if we reading indexes
            read_value = manual_input.read_int
            n = layers - 1
        else:  # if we reading speed
            read_value = manual_input.read_float
            n = layers

        values: List[Any] = []
        for _ in range(n):
            value = read_value(message=message)
            while value <= 0 or value in values:
                self.poutput("Value must be positive and do not repeat")
                value = read_value(message=message)
            values.append(value)
        return values

    def _calculate(self, speed: Any, indexes: List[int] = None):
        """Calculate structure depth. API for automatic calculation in case
        we already have all needed data (for future modules).

        Parameters
        ----------
        speed : TODO
        indexes : TODO

        Returns
        -------
        TODO

        """
        self._datafile.points["Depth"] = depth.calculate(
            self._datafile.points["Time"], speed, indexes
        )
