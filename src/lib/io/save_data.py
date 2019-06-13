import os

from .. import data


def save(path: str, datafile: data.Data):
    """TODO: Docstring for save.

    Parameters
    ----------
    path : TODO

    Returns
    -------
    TODO

    """
    if os.path.isdir(path):
        datafile.points.to_csv(
            path_or_buf=os.path.abspath(path) + "/" + datafile.name + ".csv",
            index=False,
        )
    else:
        datafile.points.to_csv(path_or_buf=os.path.abspath(path) + ".csv", index=False)
