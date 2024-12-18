#!/usr/bin/env python3
"""basic async module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random period between 0 and max_delay"""
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
