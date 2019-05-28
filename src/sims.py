#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: main.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description: Program for easing work with Secondary Ion Mass Spectrometry data.
"""
import os

import calculator
import cmd2
import plot_settings
from modules import db
from modules import depth
from modules import file_read
from modules import manual_input
from modules import minor


class Main(cmd2.Cmd):

    """Main CLI class """

    prompt = ">>> "
    intro = "Welcome to SIMS! Type ? to list commands."

    CMD_CAT_GRAPH = "Graph"
    CMD_CAT_DATA = "Work with data"
    CMD_CAT_MATHEMATICA = "Mathematica"

    default_to_shell = True

    def __init__(self):
        super().__init__()

    @cmd2.with_category(CMD_CAT_MATHEMATICA)
    def do_calculator(self, _):
        """Helpful Calculator

        Returns
        -------
        TODO

        """
        calculator.Calculator()

    def do_clear(self, _):
        """Clear the terminal screen"""
        os.system("clear")

    @cmd2.with_category(CMD_CAT_DATA)
    @cmd2.with_argument_list
    def do_open(self, args):
        """Open file"""
        if not args:
            self.perror("You must specify the file path!")
            return
        self.datafile = file_read.asc(args[0])
        print(self.datafile)

    complete_open = cmd2.Cmd.path_complete

    @cmd2.with_category(CMD_CAT_DATA)
    def do_data(self, _):
        """Print current datafile"""
        try:
            print(self.datafile)
        except Exception:
            print("Data file is not loaded")

    @cmd2.with_category(CMD_CAT_DATA)
    def do_depth(self, _):
        """Calculate depth"""
        try:
            self.datafile.points["Depth"] = depth.set_arguments_and_calculate(
                self.datafile.points["Time"]
            )
        except Exception as e:
            print("{}".format(e))

    @cmd2.with_category(CMD_CAT_DATA)
    def do_concentration(self, _):
        """TODO: Docstring for do_concentration.

        :_: TODO
        :returns: TODO

        """
        matrix = self.select(self.datafile.y, "Select matrix: ")
        self.datafile.set_matrix(matrix)
        impurity = self.select(self.datafile.impurities, "Select impurity: ")
        ia = db.get_ia(impurity)
        rsf = manual_input.read_float(message="Input RSF: ")
        element = db._strip_ion(impurity)
        try:
            result = minor.concentration(
                self.datafile.points[impurity], ia, self.datafile.points[matrix], rsf
            )
            self.datafile.points[element] = result
        except Exception as e:
            print(f"{e}")

    @cmd2.with_category(CMD_CAT_GRAPH)
    def do_plot(self, _):
        """Plot points from datafile"""
        try:
            self.datafile.plot()
        except Exception as e:
            print(f"{e}")

    @cmd2.with_category(CMD_CAT_GRAPH)
    def do_plot_settings(self, _):
        """Plot Settings"""
        plot_settings.PlotSetup(self.datafile)


if __name__ == "__main__":
    Main().cmdloop()
