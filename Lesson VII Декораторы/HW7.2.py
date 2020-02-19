"""
2. Напишите параметризованный декоратор для классов,
 который будет считать и выводить время работы
 методов класса, имена которых переданы в параметрах декоратора.
"""

from functools import wraps
from time import sleep, time


def dec(name_method):
    def decorator(klass):
        old_foo = klass.__dict__.get(name_method)

        @wraps(klass.__dict__.get(name_method))
        def decorated_foo(self, *args, **kwargs):
            start = int(round(time() * 1000))
            old_foo(self, *args, **kwargs)
            end = int(round(time() * 1000))
            print("Время работы: {}".format(end-start))
        setattr(klass, name_method, decorated_foo)
        return klass

    return decorator


@dec('inspect')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


a = Spam(2)
a.inspect()
a.foo()