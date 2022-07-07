import random


def get_words():
    with open('text.txt', "r") as file:
        return file.read().splitlines()


def simple_word(word):
    word_list = list(word)
    random_word = random.sample(word_list, len(word_list))
    return ''.join(random_word)


def save_result(name, points):
    with open('history.txt', "a") as file:
        file.write(f'{name} {points}\n')


def statistics(filename):
    with open(filename, "r") as file:
        stats = file.read().splitlines()
    game_count = 0
    max_points = 0
    for result in stats:
        user_name, points = result.split()
        if max_points < int(points):
            max_points = int(points)
        game_count += 1
    return {'game_count': game_count, 'max_points': max_points}
