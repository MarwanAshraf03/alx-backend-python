#!/usr/bin/env python3
"""same first element module"""
import typing
import types


# The types of the elements of the input are not know
def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing[typing.Any | types.NoneType]:
    if lst:
        return lst[0]
    else:
        return None