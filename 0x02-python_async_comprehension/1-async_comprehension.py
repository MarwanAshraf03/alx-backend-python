#!/usr/bin/env python3
"""Module"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    uses async comprehension to collect 10 numbers
    from async_generator function
    """
    ll: typing.List[float] = [i async for i in async_generator()]
    return (ll)
