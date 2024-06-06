#!/usr/bin/env python3
"""_summary_
    """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiplier_function(value: float) -> float:
        """_summary_

        Args:
            value (float): _description_

        Returns:
            float: _description_
        """
        return value * multiplier

    return multiplier_function
