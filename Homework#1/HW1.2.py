# Напишите программу Python для подсчета количества символов
# (частоты символов) в строке.
# Пример строки : google.com
# Ожидаемый результат: {'o': 3,' g': 2,'.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


frequency = {}
frequency_sorted = {}
word = input("Enter string:");
print(word);

for i in word:
    count = frequency.get(i, 0)
    frequency[i] = count + 1


for i in sorted(frequency.items(), key=lambda kv: kv[1], reverse=True) :
    frequency_sorted[i] = i;

print(frequency_sorted)

