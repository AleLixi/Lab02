from fnmatch import translate, fnmatch
import fnmatch
from dictionary import Dictionary



class Translator:

    def __init__(self,dictionary_file="dictionary.txt"):
        self.dictionary = Dictionary(dictionary_file)


    def printMenu(self):
        print("Menu:")
        print(" 1. Aggiungi nuova parola")
        print(" 2. Cerca una traduzione")
        print(" 3. Cerca con wildcard")
        print(" 4. Exit")
        print("Scegli un numero: ")


    def loadDictionary(self, file_path):
        try:
            with open("dictionary.txt", "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split()
                    word_aliena = parts[0]
                    word_translation = parts[1:]
                    self.dictionary.words[word_aliena] = list(word_translation)
        except FileNotFoundError:
            print("Il file non esiste ancora. Verrà creato automaticamente.")

    '''def handleAdd(self, tupla):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        word_aliena , word_translate = tupla.split(maxsplit=1)
        if word_aliena in self.dictionary.words or any(trad in self.dictionary.reversed_words for trad in word_translate):
            print("la parola esiste già nel dictionary, aggiungere significato?")
            print("1. Si")
            print("2. No")
            answer_countinues = input()
            if int(answer_countinues) == 1:
                self.dictionary.words[word_aliena].extend(word_translate)
                with open("dictionary.txt", "r+", encoding="utf-8") as file:
                    lines = file.readlines()
                    file.seek(0)  # Torna all'inizio del file
                    for line in lines:
                        parts = line.strip().split()
                        if parts and parts[0] == word_aliena:
                            # Se la parola aliena è già nel file, aggiorna le sue traduzioni
                            file.write(f"{word_aliena} {' '.join(self.dictionary.words[word_aliena])}\n")



        else:
            if word_aliena.isalpha() and all(trad.isalpha() for trad in word_translate):
                self.dictionary.words[word_aliena] = list(word_translate)
                with open("dictionary.txt", "a", encoding="utf-8") as file:
                    file.write(f"\n{word_aliena} {word_translate}")
                        print(f"aggiunta la parola {word_aliena} con la traduzione {word_translate} al dictionary")'''

    def handleAdd(self, tupla):
       # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
       word_aliena, word_translate = tupla.split(maxsplit=1)
       word_translate = word_translate.split()  # Assicurati che word_translate sia una lista di parole

       # Se la parola aliena esiste già nel dizionario, chiedi se vuoi aggiungere altre traduzioni
       if word_aliena in self.dictionary.words:
           self.dictionary.words[word_aliena].extend(word_translate)

           # Apre il file in modalità "r+" per leggere e scrivere senza sovrascrivere tutto
           with open("dictionary.txt", "r+", encoding="utf-8") as file:
               lines = file.readlines()  # Legge tutte le righe del file
               file.seek(0)  # Torna all'inizio del file
               updated = False

               # Scorri le righe e aggiorna solo la riga della parola aliena
               for line in lines:
                   parts = line.strip().split()
                   if parts and parts[0] == word_aliena:
                       # Se la parola aliena è nel file, aggiorna la sua traduzione
                       file.write(f"{word_aliena} {' '.join(self.dictionary.words[word_aliena])}\n")
                       updated = True
                   else:
                       # Scrivi le altre righe senza modifiche
                       file.write(line)

               # Se la parola aliena non era nel file, aggiungila alla fine
               if not updated:
                   file.write(f"\n{word_aliena} {' '.join(self.dictionary.words[word_aliena])}")

       else:
           # Se la parola aliena non esiste, aggiungila come nuova parola
           self.dictionary.words[word_aliena] = word_translate
           with open("dictionary.txt", "a", encoding="utf-8") as file:
               file.write(f"\n{word_aliena} {' '.join(word_translate)}")
       print(f"Aggiunta/aggiornata la parola {word_aliena} con le traduzioni {', '.join(word_translate)} nel dizionario.")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>

        try:
            if query in self.dictionary.words:
                return self.dictionary.translate(query)  # Se self.dictionary è un'istanza di Dictionary
        except KeyError:
            return "parola non trovata"

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        risultati = []

        for parola_aliena in self.dictionary.words:
            if fnmatch.fnmatch(parola_aliena, query):  # Troviamo le parole corrispondenti
                risultati.append(self.dictionary.words[parola_aliena])  # Prendiamo la traduzione

        return risultati  # Restituiamo solo le traduzioni