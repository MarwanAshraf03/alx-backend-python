#!/usr/bin/env python3
"""Module"""
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> list:
    """function"""
    zoomed_in: list = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: list = zoom_array(array)

zoom_3x: list = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)