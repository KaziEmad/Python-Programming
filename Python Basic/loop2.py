# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:43:03 2022

@author: kazie
"""

grocery_list = ["Onion", "Ginger", "Tomato", "Water"]

print("Loop 1:")
for item in grocery_list:
    # print(item)
    if item == "Tomato":
        continue
    print(item)

print("Loop 2:")
for i in range(0, len(grocery_list)):
    print(grocery_list[i])

print("Loop 3:")
for i in range(0, 10, 2):
    print(i)