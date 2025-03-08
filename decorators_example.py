import time
'''
Написати декоратор, який буде ловити помилки
'''

def catch_error(func):
    def wraps(*args, **kwargs):
        try:
            print(func.__name__)
            return func(*args, **kwargs)
    
        except Exception:
            print(f"Exception happened in function {func.__name__}")
    return wraps


'''
Написати декоратор, який буде повторювати виклик функції, якщо вона повернула помилку
'''
def repeat(n: int):
    attempts = 0

    def catch_error(func):
        def wraps(*args, **kwargs):
            nonlocal attempts
            while attempts < n:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Exception happened in function {func.__name__}")
                    attempts += 1
                    time.sleep(2)
            print("Tried too many attempts to run the function")
        return wraps
    return catch_error

@repeat(5)
def sum_numbers(a: int, b: int) -> int:
    '''Function to calculate a sum of numbers'''
    # raise ValueError
    return a + b



print(sum_numbers(a=1, b=2))
# print(sum_numbers(a=1, b=2))
# print(sum_numbers(a=1, b=2))
