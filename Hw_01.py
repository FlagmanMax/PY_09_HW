# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

# modifications:
# 01 Сделал функцию get_non_zero_rand() для генерации случайного числа, за исключением 0.
# 02 Для исключения генерации пустых строк в csv файле  нужно при открытии файла добавить "newline=''"
#   т.к. The csv.writer module directly controls line endings and writes \r\n into the file directly.

from random import choice, randint
import csv
import json

def csv_reader(path: str = 'abc.csv') -> list[tuple]:
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, dialect='excel', delimiter=';')
        for row in reader:
            result.append(tuple(map(float,row)))
    return result

def json_writer(result: dict, path:str = "Hw_01.json"):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def deco_abc(func):
    abc_list = csv_reader('Hw_01.csv')
    def inner():
        result = {}
        for abc in abc_list:
            roots = func(abc)
            a, b, c = abc
            result[f'{a=}, {b=}, {c=}'] = roots
        return result
    return inner

def deco_json_writer(func):
    def inner():
        roots = func()
        json_writer(roots)
        return roots
    return inner


def get_non_zero_rand():
    x = 0
    while x==0:
        x = randint(-100, 100)
    return x

def generate_abc(count: int = 100):
    final_abc = []
    for _ in range(count):
        final_abc.append(
            (
                get_non_zero_rand(),
                randint(-100,100),
                randint(-100,100)
            )
        )
    with open('Hw_01.csv', 'w', encoding='utf-8', newline='') as file:
        csv.writer(file, dialect='excel', delimiter=";",).writerows(final_abc)

@deco_json_writer
@deco_abc
def square_solution(abc: tuple[int, int, int]) -> tuple:
    a, b, c = abc
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1,2), round(x2,2)
    elif d ==0:
        return (round(-b/(2*a),2),)
    else:
        return (None,)


generate_abc(100)
print(*square_solution())
