#!/usr/bin/env python3
"""mixed list module"""


# def sum_mixed_list(mxd_lst: list[float, int]) -> float:
def sum_mixed_list(mxd_lst: list[float | int]) -> float:
    return sum(mxd_lst)
