#!/usr/bin/env python3
"""Module"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """function"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
