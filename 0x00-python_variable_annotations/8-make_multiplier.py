#!/usr/bin/env python3
"""
Make a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier: a float number
    return: return a function that multiplies with mutliplier
    """
    def mult(multiplier: float) -> float:
        return 1.0 * multiplier

    return mult
