# -*- coding: utf-8 -*-
"""Instructor Demo: Lists.

This script showcases basic operations of Python Lists.
"""

colored_hats = ["green", "blue", "red", "purple"]

my_favorite_things = ["chocolate", 3, ["golf", "weights"], "breakfast_tacos"]

where_we_live = [
    "Houston", 
    "Katy", 
    "New York", 
    "Corsicana",
    "Houston 2", 
    "Katy 2", 
    "New York 2", 
    "Corsicana 2"
]

print(where_we_live)
print("---------------")

print("My hometown is... this is the first element of this list!")
print(where_we_live[0])

print("---------------")
print("Index for Houston:")
print(where_we_live.index("Houston"))

print("---------------")
print("Printing every other city")
# [start:stop:steps], [::2]
print(where_we_live[::2])

print("---------------")
print("The last city is...")
print(where_we_live[-1])

print("---------------")
print("Change the first element in the list...")
where_we_live[0] = "Austin"
print(where_we_live)

print("---------------")
print("Adding a new place to the end of the list...")
where_we_live.append("Atlanta")
print(where_we_live)

print("---------------")
atl_index = where_we_live.index("Atlanta")
where_we_live.pop(atl_index) # By index
print(where_we_live)
print("---------------")

print("Calculating the number of places...")
print(len(where_we_live))
print("---------------")