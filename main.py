# Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром
# для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

url = 'https://api.github.com/search/repositories'
params = {'q': 'html'}

response = requests.get(url, params=params)

print('Статус-код ответа:', response.status_code)
print('Содержимое ответа в формате JSON:')
pprint.pprint(response.json())