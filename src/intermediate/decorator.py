"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def decorator(func: Callable[P, R]) -> Callable[P, R]:
    return func


@decorator
def foo(a: int, *, b: str) -> None:
    ...

@decorator
def bar(c: int, d: str) -> None:
    ...

foo(1, b="2")
bar(c=1, d="2")

foo(1, "2") # type: ignore
foo(a=1, e="2") # type: ignore[call-arg]
decorator(1) # type: ignore[arg-type]
