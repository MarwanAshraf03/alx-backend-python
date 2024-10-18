#!/usr/bin/env python3
"""Module"""
import asyncio
import random
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[Any, Any]:
    """yields a random number after sleeping for 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
