#!/usr/bin/env python3

# Simpson slicing challenge
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

# Remove single words from the list above and add to a variable
eyes = trial[2].get("goggles")
print(eyes)
goggles = trial[2].get("eyes")
print(goggles)
nothing = trial[3]
print(nothing)

print(f"My {eyes}, the {goggles} do {nothing}!")
