#!/usr/bin/env python3
"""_summary_
    """

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return delays