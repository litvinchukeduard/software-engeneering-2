from math import pi
import math

# import variables
# from variables import counter

# pi = 3.16
# print(pi)
# print(math.pi)

def my_function():
    global pi
    pi = 3.16
    print(pi)

my_function()
print(pi)
print(math.pi)
