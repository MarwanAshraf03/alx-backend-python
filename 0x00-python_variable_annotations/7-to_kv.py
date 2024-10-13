#!/usr/bin/env python3
"""tuple module"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    to_kv: returns a tuple in the format (k, v^2)
    k: string
    v: integer or float
    """
    return (k, v ** 2)
