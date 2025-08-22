"""
TODO:

Define a class `Person` that represents a dictionary with five string keys:
    name, age, gender, address, email

The value of each key must be the specified type:
    name - str, age - int, gender - str, address - str, email - str

Note: Only `name` is required
"""

from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]

a1: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com"
}
a2: Person = {"name": "Capy"}
a3: Person = {"age": 1, "gender": "Male", "address": "", "email": ""} # type: ignore[typeddict-item]
