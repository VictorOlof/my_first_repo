import random
from turtle import *


def main():
    words = ["apple", "banana", "watermelon", "strawberry"]
    word = random.choice(words)
    hidden_word = "_ " * len(word)
    print(hidden_word)
    lives = 8
    used_letters = ""

    # Config guessed letters characters 
    guessed_letters_turtle = Turtle()
    guessed_letters_turtle.hideturtle()
    guessed_letters_turtle.penup()
    guessed_letters_turtle.goto(0, -300)

    # Config "Letters used" text
    letters_used_turtle = Turtle()
    letters_used_turtle.hideturtle()
    letters_used_turtle.penup()
    letters_used_turtle.goto(0, -265)

    # Config "Print letters"/ hidden word
    hidden_word_turtle = Turtle()
    hidden_word_turtle.hideturtle()
    hidden_word_turtle.penup()
    hidden_word_turtle.goto(0, -200)

    # Config text input
    input_turtle = Turtle()
    input_turtle.hideturtle()
    screen = input_turtle.getscreen()

    # Config hangman
    hangman_turtle = Turtle()
    hangman_turtle.hideturtle()
    hangman_turtle.pensize(7)

    # Print hidden word
    hidden_word_turtle.write(f"{hidden_word}", align="center", font=("Arial", 35, "normal"))
    # Print "Letters used:"
    letters_used_turtle.write(f"Letters used:", align="center", font=("Arial", 25, "normal"))

    while lives > 0:
        # print("You have used the letters:", used_letters)
        guessed_letters_turtle.clear()
        guessed_letters_turtle.write(f"{used_letters}", align="center", font=("Arial", 25, "normal"))

        # guessed_letter = input("Enter a letter: ")
        guessed_letter = screen.textinput("Enter a letter", "Letter:")
        used_letters += guessed_letter + " "

        new_hidden = ""
        lose_life = True
        for i, character in enumerate(word):
            if guessed_letter.lower() == character:
                new_hidden += character + " "
                lose_life = False
            else:
                new_hidden += hidden_word[i * 2] + " "

        if lose_life:
            lives -= 1

            hideturtle()
            penup()
            pensize(7)
            goto(-160, -150)
            pendown()
            left(90)
            forward(450)
            right(90)
            forward(250)
            right(90)
            forward(40)
            right(90)
            pensize(4)
            circle(50)
            left(90)
            penup()
            forward(100)
            pendown()
            forward(120)
            left(40)
            forward(100)
            left(180)
            forward(100)
            right(260)
            forward(100)
            right(180)
            forward(100)
            left(40)
            forward(100)
            left(120)
            forward(100)
            right(180)
            forward(100)
            right(60)
            forward(100)

        hidden_word = new_hidden

        # print(hidden_word)
        hidden_word_turtle.clear()
        hidden_word_turtle.write(f"{hidden_word}", align="center", font=("Arial", 35, "normal"))

        # print("Lives:", lives)

        if "_" not in hidden_word:
            # print("You did it!!!")
            break
    done()


if __name__ == '__main__':
    main()
