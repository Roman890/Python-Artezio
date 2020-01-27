# Напишите скрипт Python для объединения двух словарей Python

dictionary_1 = {'a': 10, 'b': 20}
dictionary_2 = {'c': 30, 'd': 40}
new_dictionary = dict(list(dictionary_1.items()) + list(dictionary_2.items()))
print(new_dictionary)