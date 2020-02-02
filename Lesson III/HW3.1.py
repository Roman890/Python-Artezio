"""
1. Написать несколько функций, которые в качестве единственного аргумента
принимают список (или кортеж) целых чисел.
"""


def function_1(list_param):
    """функция должна вернуть квадраты элементов коллекции"""
    new_list = list_param
    new_list_2 = []
    for i in new_list:
        new_list_2.append(pow(i, 2))
    return new_list_2


def function_2(list_param):
    """функция должна вернуть только элементы на четных позициях"""
    new_list = list_param
    new_list_2 = []
    for i, j in enumerate(new_list):
        if i % 2 == 0:
            new_list_2.append(j)
    return new_list_2


def function_3(list_param):
    """функция возвращает кубы четных элементов на нечетных позициях"""
    new_list = list_param
    new_list_2 = []
    for i, j in enumerate(new_list):
        if j % 2 == 0 and i % 2 != 0:
            new_list_2.append(pow(j, 3))
    return new_list_2


print("Результат функции №1 : ", function_1([1, 2, 3, 4, 5]))
print("Результат функции №2 : ", function_2([1, 2, 3, 4, 5]))
print("Результат функции №3 : ", function_3([1, 2, 3, 4, 5]))
