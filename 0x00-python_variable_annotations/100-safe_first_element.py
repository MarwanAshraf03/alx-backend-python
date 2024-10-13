#!/usr/bin/env python3
"""same first element module"""
# import typing
from typing import Union, Any, Sequence
import types


# The types of the elements of the input are not know
# def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any | types.NoneType]:
def safe_first_element(lst: Sequence[Any]) -> Union[types.NoneType, Any]:
    if lst:
        return lst[0]
    else:
        return None