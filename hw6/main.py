from functions import get_words, simple_word, save_result, statistics


def main():
    user_name = input('Введите ваше имя ')
    words = get_words()
    points = 0

    for word in words:
        shuttled_word = simple_word(word)
        print(f'Угадайте слово: {shuttled_word}')
        user_input = input()

        if word == user_input:
            points += 10
            print(f'Верно! Вы получаете 10 очков.')
        else:
            print(f'Неверно! Верный ответ – {word}.')

    save_result(user_name, points)
    game_result = statistics('history.txt')
    print(f'Всего игр сыграно: {game_result["game_count"]}')
    print(f'Максимальный рекорд: {game_result["max_points"]}')


if __name__ == '__main__':
    main()
