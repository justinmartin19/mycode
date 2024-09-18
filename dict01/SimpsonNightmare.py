#!/usr/bin/env python

# Simpson slicing nightmare

# List of words to pull from
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# Words pulled from list above and put into variables
eyes = print(nightmare.get("first"))
print(eyes)
goggles = nightmare.get("kumquat")
print(goggles)
nothing = nightmare.get("d")
print(nothing)

print(f"my {eyes}, the {goggles} do {nothing}!")
