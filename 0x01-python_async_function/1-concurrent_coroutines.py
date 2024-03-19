#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """
    Running multiple random wiats
    """
    delays: List = []
    for _ in range(n):
        delay: float = await wait_random(max_delay)
        if delays == []:
            delays.append(delay)
        elif delay < delays[0]:
            delays = [delay] + delays
        elif delay > delays[-1]:
            delays = delays + [delay]
        else:
            for i in range(len(delays) - 1):
                if delay >= delays[i] and delay < delays[i + 1]:
                    delays = delays[:i + 1] + [delay] + delays[i + 1:]

    return delays
