#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """

import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """_summary_

    Yields:
        _type_: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
