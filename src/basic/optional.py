"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""

from typing import Union, Optional


def foo(x: Optional[int] = 1):
    pass

foo(10)
foo(None)
foo()

foo("10") # type: ignore[arg-type]
