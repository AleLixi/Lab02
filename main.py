import translator as tr
from dictionary import Dictionary

t = tr.Translator()

dictionary = Dictionary("dictionary.txt")

while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    if not txtIn.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

        # Add input control here!

    if int(txtIn) == 1:
        print("digita quale parola vuoi aggiungere:")
        txtIn = input().lower()
        t.handleAdd(txtIn)
        print("parola aggiunta correttamente, vuoi fare altro?")
        print("1. Si")
        print("2. No")
        answer_countinues = input()
        if int(answer_countinues) == 1:
            t.printMenu()
        else :
            break
    if int(txtIn) == 2:
        boolean = True
        while(boolean):
            print("digita quale parola vuoi cercare:")
            txtIn = input().lower()
            if txtIn in dictionary.words:
                print(t.handleTranslate(txtIn))
                print("vuoi eseguire altre azioni?")
                print("1. Si, cerca altre parole")
                print("2. si, tornare al menu principale")
                print("3. No,esci")
                answer_countinues = input()
                if int(answer_countinues) == 2:
                    boolean = False
                    t.printMenu()
                if int(answer_countinues) == 1:
                    txt = input().lower()
                    print(t.handleTranslate(txt))
            else:
                print("parola non trovata :(")
                print("vuoi cercare altre parole?")
                print("1. Si")
                print("2. No")
                answer_countinues = input()
                if int(answer_countinues) == 1:
                    t.printMenu()
                else:
                    boolean = False
                    break


    if int(txtIn) == 3:
        print("digita quale parola vuoi cercare:")
        wildcard = input().lower()
        results = t.handleWildCard(wildcard)
        if len(results) == 0:
            print("Nessuna parola trovata")
        else:
            print(results)

    if int(txtIn) == 4:
        break

    else :
        print("Per favore, inserisci un numero valido.")
        continue