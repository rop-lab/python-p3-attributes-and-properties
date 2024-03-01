#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) >= 25:
            raise ValueError("Name must be a string and less than 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError(f"{value} is not an approved dog breed.")

d1 = Dog("Rusty", "Mastiff")
print(d1.name)  # Rusty
d1.name = "Max"
print(d1.name)  # Max

try:
    d1.name = 987654321
except ValueError as e:
    print(e)  # Name must be a string and less than 25 characters.

try:
    d1.breed = "Labrador"
except ValueError as e:
    print(e)  # Labrador is not an approved dog breed.
    pass
