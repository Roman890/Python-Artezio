# Написать программу, которая принимает от пользователя имя и пароль.
# Сравнивает пароль с заданным в коде.
# 	В случае совпадения печатает в консоль
# 	"Password for user: <Имя пользователя> is correct"
# 	Если пароль не совпадает, то печатает в консоль
# 	"Password for user: <Имя пользователя> is incorrect"
# 	"Please try again..."
# 	И снова запрашивает пароль (не завершается).

username = str(input("Введите имя пользователя: "))

while True :
    password = str(input("Введите пароль: "))
    if (password == "123"):
        print("Пароль для пользователя: ", username, " верный")
        break
    else :
        print("Пароль для пользователя: ", username, " не верный")
        print("Пожалуйста, повторите еще раз...")