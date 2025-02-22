'''
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

'''

def accum(arg: str) -> str:
    result_list = []
    for index, symbol in enumerate(arg):
        # print(arg.index(symbol))
        result_list.append((symbol * (index + 1)).capitalize())
    return '-'.join(result_list)

# print('hello world'.capitalize())

my_list = ['a', 'b', 'c'] # a b c
# print(' hello '.join(my_list))
print(accum("abcd"))
# print('hello world' * 5)
