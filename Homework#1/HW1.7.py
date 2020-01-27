# Напишите скрипт Python для объединения двух словарей Python

x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
z = dict(list(x.items()) + list(y.items()))
print (z)