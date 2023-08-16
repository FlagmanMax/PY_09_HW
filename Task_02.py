# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint

def main(func):
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


@main
def guess_num(stop, tries):
    """

    :param start:
    :param stop:
    :param tries:
    :return:
    """
    # print('04>>@func')

    start = 1
    num = randint(start, stop + 1)

    print(f"Угадай число от {start} до {stop} за {tries} попыток!")

    counter = 0
    while counter < tries:
        counter += 1

        guess = int(input("Введи число: "))
        if guess == num:
            print(f"Угадал за {counter} попыток")
            break
        elif guess < num:
            print("У меня больше")
        else:
            print("У меня меньше")

    else:
        print(f"Не угадал число {num}")

# print("02>>@code")

guess_num(100,10)