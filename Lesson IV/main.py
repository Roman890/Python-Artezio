"""главная функция"""
from website_alive import check_response


web_site = input("Введите адрес сайта: ")
if check_response.check(web_site):
    print('Сайт доступен')
else:
    print('Сайт не доступен')
