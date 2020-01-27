# Напишите программу на Python, чтобы найти самые
# высокие 3 значения в словаре

my_dict = {'a':10, 'b':843, 'c': 39, 'd' : 150}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)