"""
Напишите итератор EvenIterator,
который позволяет получить из списка все элементы,
стоящие на чётных индексах.
"""


class EventIterator(object):
    """итератор для четных индексов"""
    def __init__(self, new_list):
        self.new_list = new_list
        self.i = -2

    def __iter__(self):
        self.i = -2
        return self

    def __next__(self):
        self.i += 2
        if self.i % 2 == 0 and self.i < len(self.new_list):
            return self.new_list[self.i]
        raise StopIteration


ITER = EventIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in ITER:
    print(i)
