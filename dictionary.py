

class Dictionary:

    def __init__(self, file_path : str):
        self.file_path = file_path
        self.words={}
        self.reversed_words={}
        self.loadDictionary()

    def loadDictionary(self):
        try:
            with (open(self.file_path, "r", encoding="utf-8") as file):
                for line in file:
                    parts = line.strip().split()
                    word_aliena = parts[0]
                    word_translate = parts[1:]
                    self.words[word_aliena] = word_translate
        except FileNotFoundError:
            print("Il file non esiste ancora. Verrà creato automaticamente.")







    def translate(self, word_aliena):
        if word_aliena in self.words:
            return self.words[word_aliena]
        else:
            return "parola non trovata"


    def translateWordWildCard(self):
        pass