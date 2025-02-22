'''
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
Examples

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.


'''

def high_and_low(numbers_str: str) -> str:
    numbers_list = []
    for number_str in numbers_str.split():
        numbers_list.append(int(number_str))
    # print(sorted(numbers_list))
    # return numbers_list.sort()
    numbers_list.sort()
    # print(numbers_list)
    # return numbers_list[0] numbers_list[len(numbers_list) - 1]
    return f'{numbers_list[-1]} {numbers_list[0]}'
    

# high_and_low("5 4 3 2 1")
# print([1, 2, 3][-3])

assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
