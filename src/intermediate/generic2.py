"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""
from typing import TypeVar

T = TypeVar("T", str, int)

def add(a: T, b: T) -> T:
    return a


from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"]) # type: ignore[type-var]
add(1, "2") # type: ignore[type-var]
