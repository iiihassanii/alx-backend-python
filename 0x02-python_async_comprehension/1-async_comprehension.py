#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """_summary_

    Returns:
        _type_: _description_
    """
    return [result async for result in async_generator()]
