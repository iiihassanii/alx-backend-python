#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """_summary_
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
