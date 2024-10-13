#!/usr/bin/env python3
"""same first element module"""
# import typing
from typing import Union, Any, Sequence, TypeVar
import types


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function"""
    if lst:
        return lst[0]
    else:
        return None
