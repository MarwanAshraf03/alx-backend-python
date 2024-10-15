#!/usr/bin/env python3
"""basic async module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """waits for a random period between 0 and max_delay"""
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    retlst: list[float] = [await task for task in asyncio.as_completed(tasks)]
    return retlst
