"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""

from typing import TypedDict


Student= TypedDict("Student", {"name": str, "age": int, "school": str})


a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
b: Student = {"name": 1, "age": 15, "school": "Hogwarts"} # type: ignore[typeddict-item]
c: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"} # type: ignore
d: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"} # type: ignore[typeddict-item]
e: Student = {"name": "Tom", "age": "2"} # type: ignore[typeddict-item]
assert Student(name="Tom", age=15, school="Hogwarts") == dict(name="Tom", age=15, school="Hogwarts")
