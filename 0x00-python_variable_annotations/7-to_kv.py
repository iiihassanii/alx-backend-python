#!/usr/bin/env python3
"""_summary_
    """
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (str): _description_
        v (int  |  float]): _description_

    Returns:
        Tuple: _description_
    """
    return (k, float(v ** 2))
