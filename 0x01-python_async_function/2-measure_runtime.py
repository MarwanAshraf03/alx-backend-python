#!/usr/bin/env python3
"""basic async module"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """measures the elapsed time"""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return (end - start)/n
