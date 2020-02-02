"""
3. Написать функцию, которая будет принимать только 4 позиционных аргументы
   (все аргументы числовые).
   Функция должна вернуть среднее арифметическое аргументов
   и самый большой аргумент за все время вызовов этой функции.
"""


def function():
    """внешняя функция"""
    max_num = 0

    def mean(num_1, num_2, num_3, num_4):
        """внутренняя функция"""
        max_num_2 = max(max(num_1, num_2), max(num_3, num_4))
        nonlocal max_num
        if max_num_2 > max_num:
            max_num = max_num_2
        new_sum = (num_1 + num_2 + num_3 + num_4) / 4
        return new_sum, max_num
    return mean


maxMean = function()
print(maxMean(1, 2, 3, 4))
print(maxMean(-3, -2, 10, 1))
print(maxMean(7, 8, 8, 1))
