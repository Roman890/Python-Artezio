"""модуль make_request"""
import requests


def get(url):
    """функция делает запрос на сайт"""
    return requests.get(url)
