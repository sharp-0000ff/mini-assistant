import datetime as dt

import requests

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка',
    'Андрей': 'Минск',
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    elif friends_count >= 5:
        return f'{friends_count} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    time = city_time.strftime('%H:%M')
    return time


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': '',
    }
    try:
        response = requests.get(url, weather_parameters)
    except requests.ConnectionError:
        return '<ошибка сети>'
    if response.status_code == 200:
        temperature = response.text.split()[1][1:]
        wind = response.text.split()[2][1:]
        return f'{temperature}, {wind}'
    else:
        return '<ошибка на сервере погоды>'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где живут все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья живут в городах: {cities_string}'
    else:
        return '<Неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<Не могу определить время в городе {city}>'
            time = what_time(city)
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            return what_weather(city)
        else:
            return '<Неизвестный запрос>'
    else:
        return f'У тебя нету друга по имени {name}'


def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    if name == 'Анфиса':
        return process_anfisa(tokens[1])
    else:
        return process_friend(name, tokens[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где живут все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Андрей, как погода?'
    ]
    for query in queries:
        print(f'{query} - {process_query(query)}')


runner()
