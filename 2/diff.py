from colorama import Fore, Back, Style

from itertools import zip_longest

import sys
import os.path

# print(Fore.RED + 'some red text')
# print(Back.CYAN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# print(Fore.RED + 'some red text' + Style.RESET_ALL)
# print("Hello")

def find_difference(file_path_one: str, file_path_two: str) -> dict[int, tuple[str, str]]:
    file_lines_one = []
    file_lines_two = []

    with open(file_path_one) as file_one:
        file_lines_one = file_one.readlines()
    
    with open(file_path_two) as file_two:
        file_lines_two = file_two.readlines()

    # max_length = max(len(file_lines_one), len(file_lines_two))

    for i, (line_a, line_b) in enumerate(zip_longest(file_lines_one, file_lines_two, fillvalue='')):
        if line_a != line_b:
            print(f'Incorrect line {i + 1}:')
            print(Fore.RED + line_a.strip())
            print(Fore.GREEN + line_b.strip() + Style.RESET_ALL)


# print(sys.argv)
if len(sys.argv) != 3:
    raise ValueError("To call diff, pass two file paths\n diff.py 2/a.txt 2/b.txt")

# file_path_one = sys.argv[1]
# file_path_two = sys.argv[2]
_, file_path_one, file_path_two = sys.argv

if not os.path.exists(file_path_one) or not os.path.exists(file_path_two):
    raise ValueError(f"One of the files '{file_path_one}', '{file_path_two}' does not exist")

find_difference(file_path_one, file_path_two)


# list_one = [1, 2, 3, 4]
# list_two = ['a', 'b', 'c']

# zip_result = zip(list_one, list_two, strict=True)
# for pair in zip_longest(list_one, list_two):
#     print(pair)
# print(next(zip_result))
# print(next(zip_result))

