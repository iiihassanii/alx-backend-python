#!/usr/bin/env python3
"""_summary_
    """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
