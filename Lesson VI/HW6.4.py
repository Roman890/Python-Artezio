"""
Написать функцию-генератор cycle которая бы возвращала циклический итератор.
"""


def cycle(new_list):
    """функция генератор"""
    i = 0
    while True:
        if i >= len(new_list):
            i = 0
        yield new_list[i]
        i += 1


LIST_1 = [1, 2, 3]
RESULT = cycle(LIST_1)
print(next(RESULT))
print(next(RESULT))
print(next(RESULT))
print(next(RESULT))
print(RESULT)
