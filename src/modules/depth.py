from typing import Any
from typing import List

import numpy


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
