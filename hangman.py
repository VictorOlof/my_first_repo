"""
Hitta ett ord, Skriv under underscore för varje bokstav, 8 liv

Så länge det finns liv kvar, upprepa:
    Gissa en bokstav
    Kolla hur många gånger bokstav förekommer, genom bokstav för bokstav
        Om bokstaven är samma som spelare gissat
            Byt ut det underscore som spelaren gissat
        Om man inte bytt något underscore
            Förlora ett liv
    Alla bokstäver rätt? Avsluta spelet
"""
import random

def main():
    words = ["volvo", "banjo", "tomato", "apple"]
    word = random.choice(words)
    lives = 8
    used_letters = ""
    hidden_word = "_ " * len(word)
    print(hidden_word)

    while lives > 0:
        print("Used letters: ", used_letters)
        gussed_letter = input("Enter a letter: ")
        used_letters += gussed_letter + " "

        new_hidden = ""
        lose_life = True
        for i, character in enumerate(word):  # för varje tecken i ordet
            if gussed_letter.lower() == character:
                new_hidden += character + " "
                lose_life = False
            else:
                new_hidden = new_hidden + hidden_word[i*2] + " "

        # om du ska förlora ett liv
        if lose_life:
            lives -= 1

        # lagra ändring i hidden_word
        hidden_word = new_hidden
        print(new_hidden)
        print("Lives: ", lives)

        if "_" not in hidden_word:  # kontrollera _ in hidden_word
            print("You did it.")
            break


if __name__ == '__main__':
    main()
