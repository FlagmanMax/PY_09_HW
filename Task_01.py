# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint

def main():
    stop, tries = int(input("Введите верхнюю границу >>> ")), int(input("Введите число попыток >>> "))
    def guess_num():
        """

        :param start:
        :param stop:
        :param tries:
        :return:
        """

        nonlocal stop
        nonlocal tries

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
            print("Не угадал")
    return guess_num

main()()
