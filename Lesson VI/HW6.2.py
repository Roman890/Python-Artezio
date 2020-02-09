"""
Написать генератор списка для получения списка всех публичных атрибутов объекта
"""

NEW_LIST = [i for i in dir(list) if not i.startswith('_')]
print(NEW_LIST)
