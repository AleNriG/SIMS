from matplotlib import pyplot as plt


class Data:

    """Object for storage  all measurement information

    For correct working points must be in form of pandas.DataFrame, and already be
    formatted (prepared column names).

    """

    def __init__(self, name, points):
        """Initialize filename, datapoints of measurement,
        absciss and ordinate for future plotting.

        :name: filename
        :points: pandas.DataFrame datapoints

        """
        self.name = name
        self.points = points

        self.x = "Time"
        """If add new ordinate points (for example Depth), it will be plotted
        on the plot as absciss value. To fix that, all absciss have their own list."""
        self.y = [
            header for header in list(self.points.columns) if header is not self.x
        ]

    def _plot_init(self):
        """Initializationi and Reinitilization of pyplot figure."""
        self.figure = self.points.plot(
            x=self.x, y=self.y, title=self.name, grid=True, logy=True
        )
        self.figure.set(xlabel=self.x, ylabel="Intencity")

    def __str__(self):
        border = "*".center(50, "*")
        info = "{0}\nFilename: {1}\n{0}\n{2}".format(border, self.name, self.points)

        return info

    def plot(self):
        """Plot figure."""
        self._plot_init()
        plt.show()
