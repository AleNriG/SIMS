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
from modules import depth
from modules import file_read
from modules import manual_input
from modules import minor


class Main(cmd2.Cmd):

    """Main CLI class"""

    prompt = ">>> "
    intro = "Welcome to SIMS! Type ? to list commands."

    default_to_shell = True

    def __init__(self):
        super().__init__()

    def do_clear(self, _):
        """Clear the terminal screen"""
        os.system("clear")

    def do_RSF(self, _):
        """Calculate RSF"""
        dose = manual_input.read_float(message="Input dose: ")
        integer = manual_input.read_float(message="Input integration result: ")
        try:
            result = minor.rsf(dose=dose, integer=integer)
            print("result = {:.2e}".format(result))
        except Exception as e:
            print("{}".format(e))

    def do_HMR(self, _):
        """Calculate HMR"""
        mass_1 = manual_input.read_eval(message="Input expression for the first mass: ")
        mass_2 = manual_input.read_eval(
            message="Input expression for the second mass: "
        )
        try:
            result = minor.hmr(mass_1, mass_2)
            print("result = {}".format(int(result)))
        except Exception as e:
            print("{}".format(e))

    @cmd2.with_argument_list
    def do_read(self, args):
        """Read file"""
        if not args:
            self.perror("You must specify the file path!")
            return
        self.datafile = file_read.asc(args[0])
        print(self.datafile)

    complete_read = cmd2.Cmd.path_complete

    def do_data(self, _):
        """Print current datafile"""
        try:
            print(self.datafile)
        except Exception:
            print("Data file is not loaded")

    def do_depth(self, _):
        """Calculate depth"""
        try:
            self.datafile.points["Depth"] = depth.set_arguments(
                self.datafile.points["Time"]
            )
        except Exception as e:
            print("{}".format(e))

    def do_plot(self, _):
        """Plot points from datafile"""
        try:
            self.datafile.plot()
        except Exception as e:
            print(f"{e}")

    def do_plot_settings(self, _):
        """Set up plot settings"""
        x = self.select("Time Depth", "Choose x: ")
        try:
            self.datafile.x = x
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    Main().cmdloop()
