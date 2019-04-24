#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: manual_input.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""
from modules import decorators


@decorators.repeat_if_exception
def read_float(message=""):
    return float(input(message))


@decorators.repeat_if_exception
def read_eval(message=""):
    return eval(input(message))
