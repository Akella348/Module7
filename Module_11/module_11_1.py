import requests
from bs4 import BeautifulSoup
# сам себе придумал задачу. Цель программы получать текущую информацию о погоде в Самаре.
url = 'https://www.gismeteo.ru/weather-samara-4618/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/58.0.3029.110 Safari/537.3'} # Так как html страницы используют JS, то код может
# отличаться от запроса. Поэтому передаем с чего смотрим.
request = requests.get(url, headers=headers)
if request.status_code == 200:  # Исполнение корректное
    soup = BeautifulSoup(request.text, 'html.parser')  # Кладем исходный код страницы

    temperature_element = soup.find('temperature-value', attrs={'value':True})  # Находим первый элемент темп
    feels_like_element = soup.find('div', class_='weather-feel').find('temperature-value')
    # находим элемент температуры по ощущениям
    if temperature_element and feels_like_element:  # ищем их в сочетании
        temperature = temperature_element.attrs['value']  # достаем значение атрибута по ключу
        feels_like = feels_like_element.attrs['value']  # достаем значение атрибута по ключу
        print(f'Текущая температура в Самаре: {temperature}')
        print(f'Ощущается как: {feels_like}')
    else:
        print('Не удалось найти нужные элементы на странице.')
else:
    print(f'Ошибка: {request.status_code}. Не удалось получить данные о погоде.')
