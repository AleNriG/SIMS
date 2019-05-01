"""
TODO: Documentation
"""


class Data:

    """Docstring for Data. """

    def __init__(self, name, points):
        """TODO: to be defined1.

        :name: TODO
        :points: TODO
        :figure: TODO

        """
        self.name = name
        self.points = points
        self.figure = self.points.plot(x="Time", title=self.name, grid=True, logy=True)
        self.figure.set(xlabel="Time, [min]", ylabel="Intencity, [imp/sec]")

    def __str__(self):
        border = "*".center(50, "*")
        info = "{0}\nFilename: {1}\n{0}\n{2}".format(border, self.name, self.points)

        return info
