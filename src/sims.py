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

import cmd2
from cli import calculator
from cli import plot_settings
from modules import concentration
from modules import depth
from modules import file_read
from modules import save_data

DATA_NOT_LOADED_MSG = "There is no opened data"


class Main(cmd2.Cmd):

    """Main CLI class """

    prompt = ">>> "
    intro = "Welcome to SIMS! Type ? to list commands."

    GRAPH_GROUP = "Graph"
    DATA_GROUP = "Work with data"
    MATHEMATICA_GROUP = "Mathematica"

    default_to_shell = True

    def __init__(self):
        super().__init__()

    @cmd2.with_category(MATHEMATICA_GROUP)
    def do_calculator(self, _):
        """Helpful Calculator"""
        calculator.Calculator()

    def do_clear(self, _):
        """Clear the terminal screen"""
        os.system("clear")

    @cmd2.with_category(DATA_GROUP)
    @cmd2.with_argument_list
    def do_open(self, args):
        """Open file"""
        if not args:
            self.perror("You must specify the file path!")
            return
        self.datafile = file_read.asc(args[0])
        print(self.datafile)

    complete_open = cmd2.Cmd.path_complete

    @cmd2.with_category(DATA_GROUP)
    @cmd2.with_argument_list
    def do_save(self, args):
        """Save data to a file"""
        try:
            if not args:
                save_data.save(".", self.datafile)
            else:
                save_data.save(args[0], self.datafile)
        except AttributeError:
            print(DATA_NOT_LOADED_MSG)

    complete_save = cmd2.Cmd.path_complete

    @cmd2.with_category(DATA_GROUP)
    def do_data(self, _):
        """Print current datafile"""
        try:
            print(self.datafile)
        except AttributeError:
            print(DATA_NOT_LOADED_MSG)

    @cmd2.with_category(DATA_GROUP)
    def do_depth(self, _):
        """Calculate depth"""
        try:
            self.datafile.points["Depth"] = depth.set_arguments_and_calculate(
                self.datafile.points["Time"]
            )
        except AttributeError:
            print(DATA_NOT_LOADED_MSG)

    @cmd2.with_category(DATA_GROUP)
    def do_concentration(self, _):
        """Calculate atomic concentration of an element"""
        try:
            matrix = self.select(self.datafile.ions, "Select matrix: ")
            self.datafile.set_matrix(matrix)
            impurity = self.select(self.datafile.impurities, "Select impurity: ")
            element, result = concentration.set_arguments_and_calculate(
                self.datafile, impurity, matrix
            )
            self.datafile.points[element] = result
        except AttributeError:
            print(DATA_NOT_LOADED_MSG)

    @cmd2.with_category(GRAPH_GROUP)
    def do_plot(self, _):
        """Plot points from datafile"""
        try:
            self.datafile.plot()
        except AttributeError:
            print(DATA_NOT_LOADED_MSG)

    @cmd2.with_category(GRAPH_GROUP)
    def do_plot_settings(self, _):
        """Plot Settings"""
        plot_settings.PlotSetup(self.datafile)


if __name__ == "__main__":
    Main().cmdloop()
