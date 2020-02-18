"""
1. Напишите функцию, которая возвращает размер
  HTML документа по адресу https://google.com.
  Т.е. нужно получить страницу и вернуть ее размер (количество символов).
"""

import requests
from requests.exceptions import HTTPError


def function():
    """получить размер страницы .html"""
    url = "https://google.com"
    try:
        response = requests.get(url)
        content = response.text
        file = open('index.html', 'w')
        file.write(content)
        file.close()
        with open('index.html') as file:
            text = file.read().splitlines()
        response.raise_for_status()
        return sum(len(line) for line in text)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


print(function())
