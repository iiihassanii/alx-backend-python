#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """_summary_

    Yields:
        _type_: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
