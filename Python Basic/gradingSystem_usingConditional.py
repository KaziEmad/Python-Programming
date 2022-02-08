# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:47:42 2022

@author: kazie
"""

marks = int(input("Enter your marks: "))

def _show_grade(grade):
    print(f"You got: {grade}")

if marks >= 80:
    _show_grade("A+")
elif marks >= 70 and marks < 80:
    _show_grade("A")
elif marks >= 60 and marks < 70:
    _show_grade("A-")
elif marks >= 33:
    _show_grade("Passed")
else:
    _show_grade("F")

# Usage of "or" in condition 
if marks < 10 or marks > 80:
    print("You are either a good or a bad student")
    # nested conditionals
    if marks < 10:
        print("Bad")
    else:
        print("Excellent")
else:
    print("You are okay")
print("Finised")