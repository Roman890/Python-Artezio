# Вам дается 3 набора, найдите, является ли третий набор
# подмножеством первого и второго наборов
# Входные данные: set ([1,2]), set ([2,3), set([2])
# Ожидаемый результат: True
# Входные данные: set ([1,2]), set ([3,4), set ([5])
# Ожидаемый результат: ложь

set_1 = set([1,2])
set_2 = set([2,3])
set_3 = set([2])

if (set_3.intersection(set_2) and set_3.intersection(set_1)):
    print(True)
else :
    print(False)
