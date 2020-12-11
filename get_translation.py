import requests
import json
import settings


def get_token():
    try:
        headers = {'Authorization': 'Basic ' + settings.API_key}
        token = requests.post(settings.url_aut, headers=headers)
        token.raise_for_status()
        return token.text
    except(requests.RequestException):
        print('Сетивая ошибка')
        return False


def get_translate(word):
    try:
        headers = {'Authorization': 'Bearer ' + get_token()}
        params = {
            'text': word,
            'srcLang': 1033,
            'dstLang': 1049
        }
        req = requests.get(settings.url_translate, headers=headers, params=params)
        date = req.json()
        try:
            return date['Translation']['Translation']
        except(IndexError, TypeError):
            return False
    except(requests.RequestException):
        return False
