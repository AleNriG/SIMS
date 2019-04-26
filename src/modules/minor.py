#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: minor.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""


def hmr(mass_1: float, mass_2: float) -> float:
    return mass_2 / abs(mass_1 - mass_2)


def rsf(dose: float, integer: float) -> float:
    return dose / integer * 10 ** 7
