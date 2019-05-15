"""
TODO: Documentation
"""
from matplotlib import pyplot as plt


class Data:

    """Docstring for Data. """

    def __init__(self, name, points):
        """TODO: to be defined1.

        :name: TODO
        :points: TODO

        """
        self.name = name
        self.points = points

        self.x = "Time"

    def _plot_init(self):
        """TODO: Docstring for _plot_init.
        :returns: TODO

        """
        self.figure = self.points.plot(x=self.x, title=self.name, grid=True, logy=True)
        self.figure.set(xlabel=self.x, ylabel="Intencity")

    def __str__(self):
        border = "*".center(50, "*")
        info = "{0}\nFilename: {1}\n{0}\n{2}".format(border, self.name, self.points)

        return info

    def plot(self):
        """TODO: Docstring for plot."""
        self._plot_init()
        plt.show()
