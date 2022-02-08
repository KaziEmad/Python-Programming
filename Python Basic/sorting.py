# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:29:59 2022

@author: kazie
"""

#list
grocery_list = ["Rice", "Potato", "Tomato"]
print(grocery_list)

#sorting the items
grocery_list.sort()
print("After sorting:",grocery_list)

numbers = [5, 70, 9, 4, 2, 6]
numbers.sort()
print(numbers)

#not sorting the actual list
numbers2 = [5, 70, 9, 4, 2, 6]
sorted_list = sorted(numbers2)
print(numbers2)
print(sorted_list)