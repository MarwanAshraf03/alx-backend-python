#!/usr/bin/env python3
""""""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
    ->\
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    element_length: returns list of tuples
    lst: list of sequences
    """
    return [(i, len(i)) for i in lst]
