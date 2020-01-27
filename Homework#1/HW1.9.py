# Напишите программу Python для удаления дубликатов из списка.


def remove_duplicate(numbers):
    new_numbers = []
    for i in numbers:
        if i not in new_numbers:
            new_numbers.append(i)
    return new_numbers

print(remove_duplicate([1,2,3,2,1,1,1,1]))