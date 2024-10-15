#!/usr/bin/env python3
"""basic async module"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """waits for a random period between 0 and max_delay"""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    retlst: typing.List[float] = [await task for task in asyncio.as_completed(
        tasks)]
    return retlst
