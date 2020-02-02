"""модуль check_response"""
import requests
from website_alive import make_request


def check(url):
    """функция проверяет статус ответа"""
    page = make_request.get(url)
    if page.status_code == requests.codes.ok:
        return True
    return False
