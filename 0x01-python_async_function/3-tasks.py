#!/usr/bin/env python3
"""task_wait_random Module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """task_wait_random function"""
    return asyncio.Task(wait_random(max_delay))
