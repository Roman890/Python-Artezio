"""
2. Написать функцию, которая принимает произвольное
   количество любых аргументов. Аргументами могут быть
   вложенные списки и кортежи, содержащие числа и
   другие списки и кортежи.Пример вызова функции:
   foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11),
    b=(3, 4, [5, 6, [7, 8], []]))
   Функция должна вернуть произведение и
   сумму всех ненулевых элементов вложенных чисел.
   Возможны циклические ссылки в аргументах.
   Пример такого аргумента: a = [1, 2, 3]; a.append(a)
   При обнаружении циклической ссылки нужно
   сообщить пользователю и вернуть None.
"""


def function(*args, **kwargs):
    """Функция должна вернуть произведение и сумму
    всех ненулевых элементов вложенных чисел"""
    new_sum = 0
    new_multiple = 1
    for i in args:
        if isinstance(i, (list, tuple)):
            result = function(*i)
            if result is not None:
                new_sum += result[0]
                new_multiple *= result[1]
        else:
            new_sum += i
            if i != 0:
                new_multiple *= i
    for j, k in kwargs.items():
        if j in k:
            print("Есть циклическая ссылка")
            return None
        if isinstance(k, (list, tuple)):
            result = function(*k)
            if result is not None:
                new_sum += result[0]
                new_multiple *= result[1]
        else:
            new_sum += k
            if k != 0:
                new_multiple *= k
    return new_sum, new_multiple


print(function(1, 2, [3, 4, (5, 6, 0)],
               a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))
