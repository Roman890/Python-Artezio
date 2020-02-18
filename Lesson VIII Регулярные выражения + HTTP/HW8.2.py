"""
2. Напишите функцию, которая принимает три аргумента
  1)число, количество денег в исходной валюте, float;
  2)исходная валюта, трехсимвольная строка, str;
  3)целевая валюта, трехсимвольная строка, str;
  и возвращает количество денег в целевой валюте (тип float).
  Для получения курса валют воспользуйтесь https://api.exchangerate-api.com .

"""

import requests


def function(value, currency, currency_2):
    """конвертер валют"""
    url = 'https://api.exchangerate-api.com/v4/latest/' + currency.upper()
    response = requests.get(url)
    if response.status_code == 200 and value.is_integer():
        data = response.json()['rates']
        return data[currency_2.upper()] * value
    print("Error")
    return None


print(function(1.0, 'USD', 'RUB'))
