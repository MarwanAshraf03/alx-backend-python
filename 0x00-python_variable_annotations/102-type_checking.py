#!/usr/bin/env python3
"""Module"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> list[int]:
    """function"""
    zoomed_in: list = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)