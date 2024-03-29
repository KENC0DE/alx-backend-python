#!/usr/bin/env python3
"""
Fix code
"""
from typing import Union, TypeVar, Mapping, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Getting Fixed..."""
    if key in dct:
        return dct[key]
    else:
        return default
