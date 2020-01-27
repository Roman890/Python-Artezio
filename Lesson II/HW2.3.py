# Написать функцию вычисления факториала числа

def functionFactorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    print(factorial)

functionFactorial(int(input("Введите число: ")))