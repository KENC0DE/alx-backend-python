#!/usr/bin/env python3
"""
0. Async Generator
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generator async function
    """
    for _ in range(10):
        rand: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
