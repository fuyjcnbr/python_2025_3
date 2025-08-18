
# pep 612


from typing import TypeVar, Callable, Any
from typing_extensions import Concatenate, ParamSpec
from inspect import signature


# P = ParamSpec("P")
# T = TypeVar("T")
# T2 = TypeVar("T2")
#
# class Fn:
#     def __init__(self, f: Callable[P, T]):
#         self.f = f
#         self.sig = signature(self.f)
#         global t3
#         t3 = self.sig.return_annotation
#
#     def transform_callable(self) -> Callable[Concatenate[T2, P], t3]:
#         ...

