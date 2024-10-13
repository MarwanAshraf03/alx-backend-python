#!/usr/bin/env python3
"""same first element module"""
# import typing
from typing import Union, Any, Sequence, TypeVar
import types
new_type = TypeVar("NoneType",covariant=False, contravariant=False)

def safe_first_element(lst: Sequence[Any]) -> Union[Any, new_type.__name__]:
    if lst:
        return lst[0]
    else:
        return None