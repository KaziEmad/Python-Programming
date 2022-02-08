# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:21:43 2022

@author: kazie
"""
#funtion to check whether the number is even or odd
def is_even(number):
    if(number % 2 == 0):
        return True
    else:
        return False

#even list    
even_list = []
    
limit = int(input("Enter your limit: "))
starting = 0

while starting < limit:
    if is_even(starting):
        even_list.append(starting)   #adding items to the list
        print(f"{starting} is Even")
    else:
        print(f"{starting} is Odd")
        
    starting += 1
    
print(f"The Even List is: {even_list}")