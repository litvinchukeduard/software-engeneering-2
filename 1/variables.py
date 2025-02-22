
counter = 1 # global visibility

# min, max
# nonlocal

def my_function():
    print(counter)
    counter = 2 # function visibility
    print(counter)

def my_function_two():
    minimum_number = min([1, -1, 3])
    min = 0 # UnboundLocalError

def function_three():
    global counter
    counter += 1

function_three()
print(counter)


