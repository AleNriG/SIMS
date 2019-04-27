#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


def repeat_if_exception(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print("{}".format(e))
            return inner(*args, **kwargs)

    return inner


@repeat_if_exception
def read_float(message: str = "") -> float:
    return float(input(message))


@repeat_if_exception
def read_eval(message: str = "") -> float:
    return eval(input(message))
