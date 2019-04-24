#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: decorators.py
Author: AleNriG
Email: agorokhov94@gmail.com
Github: https://github.com/alenrig
Description:
"""
import functools


def repeat_if_exception(function):
    """TODO: Docstring for repeat."""

    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(f"{e}")
            return inner(*args, **kwargs)

    return inner


def return_ex_if_exception(function):
    """TODO: Docstring for repeat."""

    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            return f"{e}"

    return inner
