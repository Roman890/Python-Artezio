"""
Есть два списка разной длины, в одном ключи, в другом значения.
Составить словарь. Для ключей, для которых нет значений
использовать None в качестве значения. Значения, для
которых нет ключей игнорировать.
"""

key = [1, 2, 3, 4, 6, 7, 9]
value = ['a', 'b', 'c', 'd']
dictionary = {item: item_2 for id, item in enumerate(key) for id_2, item_2 in enumerate(value) if id == id_2 }

print(dictionary)
