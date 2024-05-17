# Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры
# (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for post in data:
        print(post)
else:
    print('Произошла ошибка при получении данных. Статус-код:', response.status_code)