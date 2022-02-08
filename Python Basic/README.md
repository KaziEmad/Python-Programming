# Basics of Python

- [Basics of Python](#basics-of-python)
  - [Printing the First Program](#printing-the-first-program)
  - [Input Taking in Python](#input-taking-in-python)
  - [Data Type Conversion](#data-type-conversion)
  - [Listing in Python](#listing-in-python)
  - [Function in Python](#function-in-python)
    - [Built-in Functions](#built-in-functions)
    - [Self-Define Functions](#self-define-functions)
  - [Conditionals in Python](#conditionals-in-python)
  - [Looping in Python](#looping-in-python)
    - [While Loop](#while-loop)
    - [For Loop](#for-loop)
  - [File-Operation in Python](#file-operation-in-python)


```python
"""
cd .\Python Basic\
jupyter nbconvert --to markdown Python_Basics.ipynb --output README.md
"""
```




    '\ncd .\x00numpyjupyter nbconvert --to markdown numpy.ipynb --output README.md\n'



## Printing the First Program


```python
print("Hello World!")
```

    Hello World!
    

## Input Taking in Python

The basic concepts for taking input is `input("Whatever You Want to Show in Screen while taking Input")`
- for integer `int(input("Enter Input in integer"))`
- for float `float(input("Enter Input in float"))`
- for string `input("Enter Input in Integer")`


```python
user = input("Enter Your Name")
print(f"Your Name is {user}")
```

    Your Name is Emad
    

And also there are different ways to print the output. For example:


```python
#variable for the input
user = input("Enter your name: ")

#printing the input in format 1
print("Hello " + user + "!")

#printing the input in format 2
print("Hello, %s!" % user)

#printing the input in format 3
print("Hello {}!".format(user))

#printing the input in format 4
print(f"Hello {user}!")
```

    Hello Emad!
    Hello, Emad!
    Hello Emad!
    Hello Emad!
    

## Data Type Conversion

We can easily convert data types of python. To do it, we simply need to add data type in 1st braket like `var2 = data type(var1)`


```python
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

pi_float
```

    I started with $100 and now have $194.87171000000012. Awesome!
    




    3.1415926



## Listing in Python


```python
#list
grocery_list = ["Rice", "Potato", "Tomato"]

#adding something to the list
print(grocery_list)
grocery_list.append("Water")

print(grocery_list)

#accessing the list
second_item = grocery_list[1]
print( "Second Item is",second_item)


```

    ['Rice', 'Potato', 'Tomato']
    ['Rice', 'Potato', 'Tomato', 'Water']
    Second Item is Potato
    

## Function in Python

There are two types of function in python:
- Built-in Functions
- self-define Functions

### Built-in Functions
There are a lots of builing functions in python. For example, we can sort a data using `sorted()` functions. 


```python
#list
grocery_list = ["Rice", "Potato", "Tomato"]
print(grocery_list)

#sorting the items
grocery_list.sort()
print("After sorting:",grocery_list)
```

    ['Rice', 'Potato', 'Tomato']
    After sorting: ['Potato', 'Rice', 'Tomato']
    

If we want to sort temporary, we can use below code:


```python
numbers = [5, 70, 9, 4, 2, 6]
numbers.sort()
print(numbers)

#not sorting the actual list
numbers2 = [5, 70, 9, 4, 2, 6]
sorted_list = sorted(numbers2)
print(numbers2)
print(sorted_list)
```

    [2, 4, 5, 6, 9, 70]
    [5, 70, 9, 4, 2, 6]
    [2, 4, 5, 6, 9, 70]
    

### Self-Define Functions
A self define function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. And intend(spacing) is very important in function.


```python
# self define function
def add_two_values(first, second):
    return first + second             #intend is very important in function(spacing)


number1 = 10
number2 = 3

#calling the function and adding it to a veriable sum
sum = add_two_values(number1, number2)

print(f"{number1} + {number2} = {sum}")
```

    10 + 3 = 13
    

## Conditionals in Python


```python
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


print("Finised")
```

    You got: A+
    Finised
    


```python
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
```

    You are okay
    Finised
    

## Looping in Python
- While Loop
- For Loop

### While Loop
Odd and Even using while loop


```python
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
```

    0 is Even
    1 is Odd
    2 is Even
    3 is Odd
    4 is Even
    5 is Odd
    6 is Even
    7 is Odd
    8 is Even
    9 is Odd
    10 is Even
    11 is Odd
    12 is Even
    13 is Odd
    14 is Even
    15 is Odd
    16 is Even
    17 is Odd
    18 is Even
    19 is Odd
    The Even List is: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    

### For Loop
Grocery_list Printing Using For Loop


```python
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
```

    Loop 1:
    Onion
    Ginger
    Water
    Loop 2:
    Onion
    Ginger
    Tomato
    Water
    Loop 3:
    0
    2
    4
    6
    8
    

## File-Operation in Python


```python
word_all = []
with open("input.txt", mode="r") as s_file:
    for line in s_file.readlines():
        # print(line, end="")
        # print(line.strip().split(" "))
        words = line.strip().split(" ")
        # word_all = word_all + words
        # word_all. append(words)
        word_all.extend(words)
    # print(word_all)

with open("output.txt", mode="w") as o_file:
    for word in word_all:
        o_file.write(word + "\n") # printing each word in a new line
        

        
```
