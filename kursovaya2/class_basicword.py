class BasicWord:
    def __init__(self, word, sub_word):
        self.word = word
        self.sub_word = sub_word

    def check_input_word(self, word):
        """проверку введенного слова в списке допустимых подслов (вернет bool)"""
        return word.strip().lower() in self.sub_word

    def count_sub_word(self):
        return len(self.sub_word)

    def get_word(self):
        return self.word


    def __repr__(self):
        return f"BasicWord {self.word}, {self.sub_word}"


