# Напишите программу на Python, чтобы найти самые
# высокие 3 значения в словаре

dictionary = {'a':10, 'e':50, 'b':20, 'g': 70,'c': 30, 'd' : 40,  'f':60,  'h' : 6}
result = sorted(dictionary.items(), key= lambda para:para[1], reverse=True)[:3]
print(result)