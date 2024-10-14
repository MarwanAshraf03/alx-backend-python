#!/usr/bin/env python3
"""basic async module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """waits for a random period between 0 and max_delay"""
    retlst: list[float] = []
    for _ in range(n):
        retlst.append(await wait_random(max_delay))
    return retlst
