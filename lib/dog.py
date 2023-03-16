#!/usr/bin/env python3
import ipdb

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

    def __init__(self, name = "Taco", breed = "Pointer"):  #why do these require assigned values?
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (0 < len(name) < 26):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name,)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
            
    pass



    


# class Human:

#     species = "Homo sapiens"

#     def get_age(self):
#         print("Retreieving age.")
#         return self._age

#     def set_age(self,age):
#         if(type(age) in (int, float)) and (0 <= age <= 120):
#             print(f"Setting age to {age}.")
#             self._age = age
#         else:
#             print("Age must be a number between 0 and 120.")

#     age = property(get_age, set_age,)

#     pass