"""
1.Напишите параметризованный декоратор,
 который считает и выводит при каждом вызове
 среднее время работы функции за n последних вызовов.
 Время выводить в миллисекундах.
 Пример использования:

  @average_time(n=2)
  def foo(a):
      sleep(a)
      return a

  foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
  foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
  foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."
"""

from time import sleep, time


def average_time(n):
    def outer(func):
        def wrapper(*args, **kwargs):
            all_time = 0
            for i in range(n):
                start = int(round(time() * 1000))
                result = func(*args, **kwargs)
                end = int(round(time() * 1000))
                all_time = all_time + (end - start)
            print('Среднее время работы: {:.0f} мс.'.format(all_time / n))
            return result

        return wrapper

    return outer


@average_time(n=2)
def foo(a):
    sleep(a)
    return a


print(foo(3))
print(foo(7))
print(foo(1))
