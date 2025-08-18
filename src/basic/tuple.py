"""
TODO:

foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""

def foo(x: tuple[str, int]):
    pass

foo(("foo", 1))
foo((1, 2)) # type: ignore[arg-type]
foo(("foo", "bar")) # type: ignore[arg-type]
foo((1, "foo")) # type: ignore[arg-type]
