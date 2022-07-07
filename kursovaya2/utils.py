import requests
from class_basicword import BasicWord
from random import shuffle


def load_random_word(filename):
    response = requests.get(filename)
    data = response.json()
    shuffle(data)
    random_word = data[0]

    return BasicWord(random_word['word'], random_word['subwords'])
