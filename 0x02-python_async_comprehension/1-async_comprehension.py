#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """
    returns list made with async comprehension
    """
    lst = [f async for f in async_generator()]
    return lst
