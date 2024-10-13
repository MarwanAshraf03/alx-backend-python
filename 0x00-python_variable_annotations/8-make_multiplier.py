#!/usr/bin/env python3
"""make multiplier module"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    make_multiplier: returns a function that multiplies a float by multiplier
    multiplier: float number
    """
    def ret(f: float) -> float:
        """
        ret: the returned function
        f: the float to be multiplied with multiplier
        """
        return f * multiplier
    return ret
