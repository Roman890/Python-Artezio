"""
Написать базовый класс Observable, который бы позволял наследникам:
при передаче **kwargs заносить соответствующие значения как атрибуты
сделать так, чтобы при print отображались все публичные атрибуты
"""


class Observable(object):
    """родительский класс"""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return "{}".format(
            {a: getattr(self, a) for a in dir(self) if not a.startswith('__')})

    def __getattr__(self, item):
        return self[item]


class X(Observable):
    """дочерний класс"""


CLASS_OF_KWARGS = X(foo=1, bar=5, __bazz=12, name='Amok', props=('One', 'two'))
print(CLASS_OF_KWARGS.foo)
print(CLASS_OF_KWARGS)
