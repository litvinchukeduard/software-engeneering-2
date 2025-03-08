'''

['Apples', 'Butter', 'Bread', 'Wine']

Потрібно написати функцію, яка буде знаходити продукти, що починаються на B
'''

# Розвʼязати через цикли
def find_b_words(word_list: list[str]) -> list[str]:
    result_list = []
    for word in word_list:
        if word[0] == 'B':
            result_list.append(word)
    return result_list

print(find_b_words(['Apples', 'Butter', 'Bread', 'Wine']))

# Розвʼязати через вбудовані функції (filter)
def find_b_words_build_in(word_list: list[str]) -> list[str]:
    return list(filter(lambda word: word[0] == 'B', word_list))

print(find_b_words_build_in(['Apples', 'Butter', 'Bread', 'Wine']))
# Розвʼязати через list comprehensions [x**2 for x in [1, 2, 3]]

def find_b_words_comprehensions(word_list: list[str]) -> list[str]:
    return [word for word in word_list if word[0] == 'B']

print(find_b_words_comprehensions(['Apples', 'Butter', 'Bread', 'Wine']))


# my_list = [5, 4, 3, 2, 1]
my_list = ['Apples', 'Butter', 'Bread', 'Wine']
print(sorted(my_list, key=lambda x: len(x)))
print(sorted(my_list, key=len))
# my_list = [1, 2, 3]
# print({x**2 for x in my_list})

# for x in my_list:
#     print(x ** 2)
