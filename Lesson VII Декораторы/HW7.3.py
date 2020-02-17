"""
3. Каррирование.
  Преобразовать вызов функции с конечным количеством позиционных
  аргументов f(a, b, c, d) в вызов вида f(a)(b)(c)(d),
  используя декоратор.
  Пример:
  @carry
  def foo(a, b):
        return a + b

   foo(1)(5)  # вернет 6
"""
from functools import partial
from inspect import signature


def carry(func):
    def wrapper(arg):
        if len(signature(func).parameters) == 1:
            return func(arg)
        return carry(partial(func, arg))
    return wrapper


@carry
def foo(a, b):
    return a + b


print(foo(1)(5))
