

class Words :
    def __init__(self, word_aliena, word_translate):
        self.word_aliena = word_aliena
        self.word_translate = word_translate

    def __str__(self):
        return f"{self.word_aliena} -> {self.word_translate}"