# Написать функцию, которая принимает 3 числа (a,b,c)
# и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’

def findNumber(a,b,c):
    count = 0
    if(a > b):
        temp = a
        a = b
        b = temp
    while (a != b):
        if(a % c == 0):
            count +=1
        a += 1

    print("Количество чисел, делящихся на ",c," = ",count)

findNumber(3,9,2)