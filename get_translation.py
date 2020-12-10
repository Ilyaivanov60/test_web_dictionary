import requests
import json
import settings

def get_token():

    headers = {'Authorization': 'Basic ' + settings.API_key}
    token = requests.post(settings.url_aut, headers=headers)
    if token.status_code == 200:
        return token.text
    else:
        return "не правиьлный запрос aut_Token"

def get_translate():

    headers = {'Authorization': 'Bearer ' + get_token()}
    params = {
        'text': input('ввидите слово для перевода: '),
        'srcLang': 1033,
        'dstLang': 1049
    }
    req = requests.get(settings.url_translate, headers=headers, params=params)
    print(req.status_code)
    print(req.headers["Content-Type"])
    date = req.json()
    print(date['Translation']['Translation'])

if __name__ == "__main__":
    get_translate()