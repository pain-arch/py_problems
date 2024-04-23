


# Basics
# 1. Variables

varible1 = "********************"
varible2 = "*                  *"
varible3 = "*      Welcome     *"


print()
print(varible1)
print(varible2)
print(varible3)
print(varible2)
print(varible1)


# 2. Data Types

var_1 = 10          # Integer
var_2 = 10.5        # Float
var_3 = "Hello"     # String
var_4 = True        # Boolean
var_5 = False       # Boolean
var_6 = None        # None
var_7 = [1,2,3,4,5] # List
var_8 = (1,2,3,4)   # Tuple
var_9 = {1,2,3}     # Set
var_10 = {"name":"John", "age":25} # Dictionary
var_11 = b"Hello"   # Bytes
var_12 = bytearray(10) # Bytearray
var_13 = memoryview(bytes(5)) # Memoryview

# 3. Operators

# Arithmetic Operators
# +, -, *, /, %, **, //
add = 10 + 5
sub = 10 - 5
mul = 10 * 5
div = 10 / 5
mod = 10 % 5
exp = 10 ** 5
fdiv = 10 // 5




# 4. Control Structures

# If 
a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Loops
# For Loop
for i in range(10):
    print(i)

# While Loop
i = 0
while i < 10:
    print(i)
    i += 1
    
# Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def exp(a, b):
    return a ** b

def fdiv(a, b):
    return a // b

add(10, 5)
sub(10, 5)
mul(10, 5)

# Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("John", 25)
person1.greet()


# Modules

# Importing Modules
import math
import random

# Using Modules
print(math.pi)
print(random.randint(1, 10))

# File Handling

# Writing to a file
file = open("file.txt", "w")
file.write("Hello, World!")
file.close()

# Reading from a file
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()


# Exception Handling

try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always run")

# 5. Advanced