import math 

print(math.pi)
math.pi = 3.15
print(math.pi)

def my_function():
    math.pi = 3.16

my_function()
print(math.pi)
