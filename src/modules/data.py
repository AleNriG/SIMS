"""
TODO: Documentation
"""


class Data:

    """Docstring for Data. """

    def __init__(self, name, points):
        """TODO: to be defined1.

        :name: TODO
        :points: TODO

        """
        self.name = name
        self.points = points

    def __str__(self):
        border = "*".center(50, "*")
        info = f"{border}\nFilename: {self.name}\n{border}\n{self.points}"

        return info
