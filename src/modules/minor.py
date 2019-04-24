#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: minor.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""
from modules import decorators


@decorators.return_ex_if_exception
def hmr(mass_1, mass_2):
    result = mass_2 / abs(mass_1 - mass_2)
    return int(result)


@decorators.return_ex_if_exception
def rsf(dose, integer):
    result = dose / integer * 10 ** 7
    result = f"{result:.2e}"
    return float(result)
