from class_player import Player
from utils import load_random_word

FILENAME = 'https://jsonkeeper.com/b/QN1I'


def main():
    player = Player(input('Ввведите имя игрока\n'))
    print(f"Привет, {player.user_name}")

    basic_word = load_random_word(FILENAME)
    sub_words_count = basic_word.count_sub_word()
    word_name = basic_word.get_word()
    print(f"Составьте {sub_words_count} слов из слова {word_name}\n")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print("Поехали, ваше первое слово?")

    while player.count_used_words() < basic_word.count_sub_word():
        user_input = input().lower().strip()

        if user_input in ['стоп', 'stop']:
            break
        elif len(user_input) < 3:
            print("Слишком короткое слово")
        elif not basic_word.check_input_word(user_input):
            print("Неверно")
        elif player.check_used_word(user_input):
            print("Уже использовано")
        else:
            print("Верно")
            player.add_used_words(user_input)

    if player.count_used_words() == basic_word.count_sub_word():
        print(f'Поздравляю! Тобой угаданы все слова для слова {basic_word.word}')
    else:
        total_guessed_words = player.count_used_words()
        print(f"Игра завершена, вы угадали {total_guessed_words} слов!")


if __name__ == '__main__':
    main()
