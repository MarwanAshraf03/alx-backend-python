#!/usr/bin/env python3
"""module"""
import typing


new_type = typing.TypeVar("T")
def safely_get_value(dct: typing.Mapping, key: typing.Any, default: typing.Union[new_type, None] = None) -> typing.Union[typing.Any, new_type]:
    """function"""
    if key in dct:
        return dct[key]
    else:
        return default
