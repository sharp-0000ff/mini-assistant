DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Антон': 'Минск',
}


def format_count_friends(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    elif friends_count >= 5:
        return f'{friends_count} друзей'


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
        if query == 'ты где?':
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<Неизвестный запрос>'
    else:
        return f'У тебя нету друга по имени {name}'


def process_query(query):
    temp = query.split(', ')
    if temp[0] == 'Анфиса':
        return process_anfisa(temp[1])
    else:
        return process_friend(temp[0], temp[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где живут все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
    ]
    for query in queries:
        print(f'{query} - {process_query(query)}')


runner()
