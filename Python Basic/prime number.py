# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:10:06 2022

@author: kazie
"""
import math
user_num = int(input("Enter the upper limit: "))

prime_set = set()

def is_Prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for value in range(1, user_num + 1):
    if value<10:
        if is_Prime(value):
            prime_set.add(value)
            # print(value)
    else:
        for item in prime_set:
            if value % item == 0:
                break
            else:
            prime_set.add(value)
            

for item in sorted(prime_set):
    print(item)
            
        