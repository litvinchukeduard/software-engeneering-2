from pathlib import Path
import random
'''
Написати функцію-генератор, яка буде шукати фуйли в поточній папці
'''

def generate_random_values(n: int):
    random_values = []
    for _ in range(n):
        random_values.append(random.randint(1, 10))
    for random_number in random_values:
        yield random_number

def generate_random_values_in_place(n: int):
    for _ in range(n):
        yield random.randint(1, 10)


def search_python_files_generator():
    p = Path('.')
    for file in p.glob('**/*.py'):
        yield file


# value_generator = generate_random_values(10)
# print(next(value_generator))
# print(next(value_generator))


# other_generator = generate_random_values_in_place(10)
# print(next(other_generator))
# print(next(other_generator))
# p = Path('.')
# print(p.glob('**/*.py'))

# [1, 2, 3]

for file in search_python_files_generator():
    print(file)

# search_generator = search_python_files_generator()
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))
# print(next(search_generator))

