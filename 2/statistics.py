from collections import defaultdict
'''
У файлі записані випадкові числа 5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1
Потрібно написати функцію, яка буде рахувати кількість появи кожного числа, які вона запише у файл, та виведе найчастіше число у
 термінал
'''

# 1 - Прочитати файл та вивести у зручному вигляді
# ['1', '2', '3']
# [1, 2, 3]

def read_numbers_from_file(file_path: str) -> list[str]:
    # file = open(file_path)
    with open(file_path) as file:
        return file.readline().split(', ')
    
# print(read_numbers_from_file('statistics_file.txt'))
print(read_numbers_from_file('2/statistics_file.txt'))

# 2 - Порахувати статистику по числам
# '5' -> 4
# '3' -> 5
# {'5': 4, '3': 5}
def count_statistics(elements_list: list[any]) -> dict[any, int]:
    # result_dict = {}
    result_dict = dict()
    # result_set = set()

    for element in elements_list:
        # В нашому словнику вже є таке значення
        if element in result_dict:
            result_dict[element] += 1

        # В нашому словнику ще немає такого значення
        else:
            result_dict[element] = 1

    return result_dict

def count_statistics_alt(elements_list: list[any]) -> dict[any, int]:
    result_dict = defaultdict(int)
    for element in elements_list:
        result_dict[element] += 1
    return result_dict

my_list = [1, 1, 2, 2, 3]
print(count_statistics_alt(my_list))
assert count_statistics_alt(my_list) == {1: 2, 2: 2, 3: 1}

# print(type({}))

# 3 - Запиcати у файл
'''
5: 2
3: 4
'''
def write_statistics_to_file(file_path: str, statistics_dict: dict[any, int]):
    with open(file_path, 'w') as file:
        for element, i in statistics_dict.items():
            file.write(f'{element}: {i}\n')

# 4 - Вивести найчастіше число
def find_max_item(statistics_dict: dict[any, int]) -> tuple[any, int]:
    max_element = None
    max_repetitions = 0

    for element, i in statistics_dict.items():
        if i > max_repetitions:
            max_element = element
            max_repetitions = i

    return (max_element, max_repetitions)


stats = {'1': 2, '6': 3, '2': 8}
assert find_max_item(stats) == ('2', 8)

numbers_list = read_numbers_from_file('2/statistics_file.txt')
statistics_dict = count_statistics_alt(numbers_list)
write_statistics_to_file('2/statistics_out.txt', statistics_dict)
print(find_max_item(statistics_dict))

# regular_dict = {"a": 2, "b": 4}
# print(regular_dict.items())

# regular_dict[1]

# d = defaultdict(int)
# d[1] += 1
# print(d)
