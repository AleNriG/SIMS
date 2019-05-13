from typing import Any
from typing import List

import numpy

from . import manual_input


def set_arguments(time: List[float]) -> List[float]:
    layers = manual_input.read_int(message="Input layers number: ")
    while layers <= 0:
        print("Layers value must be positive!")
        layers = manual_input.read_int(message="Input layers number: ")

    if layers == 1:
        print("Calculating depth for homostructure")
        speed = manual_input.read_float(message="Input speed: ")
        result = calculate(time, speed)

    else:
        print("Calculating depth for heterostructure")
        indexes = _get_list_of_values(
            layers, values_type="int", message="Input index of layer changing: "
        )
        speed = _get_list_of_values(
            layers, values_type="float", message="Input speed of the layer: "
        )
        result = calculate(time, speed, indexes)

    return result


def _get_list_of_values(layers: int, values_type: str, message: str) -> List[Any]:

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
            print("Value must be positive and do not repeat")
            value = read_value(message=message)
        values.append(value)
    return values


def calculate(time: List[float], speed: Any, indexes: List[int] = None) -> List[float]:
    """TODO: Docstring for calculate.

    :args: TODO
    :returns: TODO

    """
    if isinstance(speed, list) and indexes is not None:
        depth = _heterostructure(time, speed, indexes)
    elif isinstance(speed, float) and indexes is None:
        depth = _homostructure(time, speed)
    else:
        raise ValueError("Invalid variables")
    return depth


def _homostructure(time: List[float], speed: float) -> List[float]:
    """TODO: Docstring for homostructure.

    :time: TODO
    :speed: TODO
    :returns: TODO

    """
    return [i * speed for i in time]


def _heterostructure(
    time: List[float], speed: List[float], indexes: List[int]
) -> List[float]:
    """TODO: Docstring for heterostructure.

    :time: TODO
    :speed: TODO
    :indexes: TODO
    :returns: TODO

    """
    depth = [time[0] * speed[0]]
    layers = len(indexes) + 1
    indexes.append(time.index(time[-1]))
    delta_x = numpy.diff(time).mean()
    i = 0
    for layer in range(layers):
        while i < indexes[layer]:
            depth.append(depth[-1] + delta_x * speed[layer])
            i += 1
    return depth
