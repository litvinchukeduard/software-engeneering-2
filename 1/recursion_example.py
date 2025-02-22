import math
'''
Написати функцію, яка буде рахувати число у степені
'''

# power(2, 3) -> 2^3 = 2 * 2 * 2 = 8
# power(2, 3) -> 2^3 = 2 * power(2, 2) -> 2 * (2 * power(2, 1)) -> 2 * (2 * 2)
# power(2, 3) -> 2^3 = 2 * power(2, 2) -> 2 * (2 * power(2, 1)) -> 2 * (2 * (2 * power(2, 0)))

def power(number: int, p: int) -> int:
    # Перевірка на кінець рекурсії
    if p == 0:
        return 1
    # if p == 1:
    #     return number
    # Рекурсивного кроку
    # Повернення
    return number * power(number, p - 1)

def power_printed(number: int, p: int, level: int = 0) -> int:
    # Перевірка на кінець рекурсії
    if p == 0:
        print(f'power({number}, {p}) == 1 | level: {level}')
        return 1
    # if p == 1:
    #     return number
    # Рекурсивного кроку
    print(f'power({number}, {p}) ==  {number} * power_printed({number}, {p - 1}, {level + 1}) | level: {level}')
    result = number * power_printed(number, p - 1, level + 1)
    print(f'power({number}, {p}) ==  {result} | level: {level}')
    # Повернення
    return number * power(number, p - 1)

# print(power(2, 0))
# print(power(2, 1))
# print(power(2, 2))
# print(power(2, 500))

# print(pow(2, 5000))
# print(math.pow(2, 5))

power_printed(2, 3)