# Напишите программу Python для удаления дубликатов из списка.

numbers = [1,2,3,2,1,1,1,1]
new_numbers = []
for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)