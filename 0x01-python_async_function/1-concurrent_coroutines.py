#!/usr/bin/env python3
"""_summary_
    """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return delays
