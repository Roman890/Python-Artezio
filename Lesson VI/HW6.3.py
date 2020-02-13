"""
Есть два списка разной длины, в одном ключи, в другом значения.
Составить словарь. Для ключей, для которых нет значений
использовать None в качестве значения. Значения, для
которых нет ключей игнорировать.
"""

key = [1, 2, 3, 4, 6, 7, 9]
value = ['a', 'b', 'c', 'd']
dictionary = {key[i]: value[i] if i < len(value) else None for i in range(len(key))}
print(dictionary)