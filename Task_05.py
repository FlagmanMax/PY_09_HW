# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from random import randint
import json
from functools import wraps


def value_checker(func):
    # print("01>>@main")
    def wrapper(stop, tries):
        # print('03>>@wrapper')
        # stop, tries = int(input("Введите верхнюю границу >>> ")), int(input("Введите число попыток >>> "))
        if not (0 < stop <= 100 ):
            stop = randint(1, 100)
        if not (0 < tries <= 10):
            tries = randint(1, 10)
        return func(stop, tries)

    return wrapper

def json_saver(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}.json', 'a', encoding='utf-8') as file:
            temp_dict = {'args':args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            json.dump(temp_dict, file, indent=3, ensure_ascii=False)
        return result

    return wrapper

def call_count(num):
    def deco(func):
        result = []
        def wrapper(*args, **kwargs):
            for i in range(num):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return deco

# 1



# 2
@call_count(3)
@value_checker
@json_saver
def guess_num(stop, tries):
    """

    :param start:
    :param stop:
    :param tries:
    :return:
    """
    # print('04>>@func')
    result = 0

    start = 1
    num = randint(start, stop + 1)

    print(f"Угадай число от {start} до {stop} за {tries} попыток!")

    counter = 0
    while counter < tries:
        counter += 1

        guess = int(input("Введи число: "))
        if guess == num:
            print(f"Угадал за {counter} попыток")
            result = 1
            break
        elif guess < num:
            print("У меня больше")
        else:
            print("У меня меньше")

    else:
        print(f"Не угадал число {num}")

    return result

# 3
def Task_03(a,b, c='5'):
    return max(a,b,c)

# 4
def printer(string):
    print(string)
    return "OK"

guess_num(40,5)