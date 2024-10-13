#!/usr/bin/env python3
"""mixed list module"""
import typing


# def sum_mixed_list(mxd_lst: list[float | int]) -> float:
def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    return sum(mxd_lst)
