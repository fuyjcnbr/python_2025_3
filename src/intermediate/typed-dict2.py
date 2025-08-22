"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""

from typing import TypedDict, NotRequired

class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


a1: Student = {"name": "Tom", "age": 15}
a2: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a3: Student = {"name": 1, "age": 15, "school": "Hogwarts"} # type: ignore[typeddict-item]
a4: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"} # type: ignore
a5: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"} # type: ignore[typeddict-item]
a6: Student = {"z": "Tom", "age": 2} # type: ignore[typeddict-item]
assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") == dict(name="Tom", age=15, school="Hogwarts")
