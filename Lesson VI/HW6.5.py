"""
Написать функцию-генератор chain, которая последовательно
 итерирует переданные объекты
(произвольное количество)
"""


def chain(*args, **kwargs):
    """ функция генератор с произвольным количеством переданных объектов"""
    for i in args:
        yield i
    for j, k in kwargs.items():
        yield j, k


for num in chain(1, 55, 'a', k="kk"):
    print(num)
