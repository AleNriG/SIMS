#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: minor.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""
import functools


def return_ex_if_exception(function):
    """TODO: Docstring for repeat."""

    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            return f"{e}"

    return inner


@return_ex_if_exception
def hmr(mass_1, mass_2):
    result = mass_2 / abs(mass_1 - mass_2)
    return int(result)


@return_ex_if_exception
def rsf(dose, integer):
    result = dose / integer * 10 ** 7
    result = f"{result:.2e}"
    return float(result)
