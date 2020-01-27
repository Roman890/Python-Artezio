# Напишите программу Python для подсчета количества символов
# (частоты символов) в строке.
# Пример строки : google.com
# Ожидаемый результат: {'o': 3,' g': 2,'.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

frequency = {}
frequency_sorted = {}
word = input("Введите строку:")
print(word)

for i in word:
    count = frequency.get(i, 0)
    frequency[i] = count + 1

frequency_sorted = sorted(frequency.items(), key=lambda para: para[1], reverse=True)
print(dict(frequency_sorted))