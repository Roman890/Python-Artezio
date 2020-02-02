"""
5. В этом задании можно отступить от PEP8.
    Цель - выполнить задание за минимальное возможное количество
    символов в функции (если потребовался импорт отдельных модулей для функции,
    то инструкции импорта тоже считаются).
    Напишите функцию, которая будет принимать ввод пользовательской
    строки. В строке 1 или более отрицательных/положительных чисел.
"""


def find_nearest_number(number_list):
    """Функция должна вернуть ближайшее к нулю значение"""
    new_number_list = [abs(0 - x) for x in number_list]
    result_index = new_number_list.index(min(new_number_list))
    return number_list[result_index]


enter_list = list(input("Введите строку с числами:").split(" "))
enter_number_list = [float(x) for x in enter_list]
print('Ближайшее значение к 0 :', find_nearest_number(enter_number_list))
