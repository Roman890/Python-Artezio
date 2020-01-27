# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).

def range(number):
    list_1 = []
    i = 0
    while (i < number):
        list_1.append(i)
        i += 1
    return list_1

print(range(10));