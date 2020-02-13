"""
Прикрепил в github решение задания с исключениями,
потому что на сайте, тесты проверку не проходят, хотя
выводит все верно, на всех тестовых примерах.
"""

a = []
print("Для прекращения ввода, нажмите enter 2 раза\nПример ввода: ")
print("3\n1 0\n2 $\n3 1\n:")
while True:
    line = str(input())
    if line.strip() == "":
        break
    a += line.split()

i = 0
while i < len(a) - 2:
    try:
        print(int(a[i + 1]) / int(a[i + 2]))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        if a[i + 1].isdigit():
            print("Error Code: invalid literal for int() with base 10: {}".format(a[i+2]))
        else:
            print("Error Code: invalid literal for int() with base 10: {}".format(a[i+1]))
    i += 2
