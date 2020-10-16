print('Привет, я Анфиса')
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

def print_friends_count(friends_count, name=''):
    if friends_count == 1 and name != '':
        print('{}, у тебя 1 друг'.format(name))
    elif friends_count == 1 and name == '':
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4 and name != '':
        # text = str(friends_count) + ' друга'
        print('{}, у тебя {} друга'.format(name, friends_count))
    elif 2 <= friends_count <= 4 and name == '':
        print('У тебя {} друга'.format(friends_count))
    elif friends_count >= 5 and name != '':
        # text = str(friends_count) + ' друзей'
        print('{}, у тебя {} друзей'.format(name, friends_count))
    elif friends_count >= 5 and name == '':
        print('У тебя {} друзей'.format(friends_count))

print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')
