# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def call_count(num):
    def deco(func):
        result = []
        def wrapper(*args, **kwargs):
            for i in range(num):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return deco

@call_count(3)
def printer(string):
    print(string)
    return "OK"

print(printer('Ай-Ай-АЙ'))