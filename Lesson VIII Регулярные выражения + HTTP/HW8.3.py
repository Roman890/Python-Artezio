"""
3. Напишите функцию, которая получает два аргумента
  1)путь к файлу изображения jpeg на компьютере (строка);
  2)имя целевого файла (строка)
  отправляет файл HTTP POST запросом на https://postman-echo.com/post .
  В ответе будет получен файл изображения jpeg, в виде octet-stream,
  который нужно раскодировать и
  сохранить на компьютере под целевым именем, переданным в аргументе.
  Функция должна вернуть размер сохраненного файла.

  (не понял как раскодировать файл!!!)
"""

import requests


def function(path_to_file, name_file):
    """отправляет файл HTTP POST запросом на https://postman-echo.com/post"""
    url = 'https://postman-echo.com/post'
    files = {'media': open(path_to_file, 'rb')}
    result = requests.post(url, files=files)
    print(result.status_code)
    print(result.content)
    out = open(name_file, "wb")
    out.write(result.content)
    out.close()
    with open(name_file) as file:
        text = file.read().splitlines()
    return sum(len(line) for line in text)


PATH = 'C:/car.jpeg'
NAME = 'new_car.jpeg'
print(function(PATH, NAME))
