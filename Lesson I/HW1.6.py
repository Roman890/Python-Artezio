# Напишите скрипт Python для создания и печати словаря,
# содержащего число (от 1 до n) в виде (x, x*x).
# Пример словаря (n = 5) :
# Ожидаемый Результат : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

number = int(input("Введите число: "))
i = 1
dictionary = {}
while i < number+1:
    dictionary[i] = pow(i,2)
    i += 1
print(dictionary)

