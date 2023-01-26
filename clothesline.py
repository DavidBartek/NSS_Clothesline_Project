import sys

import random


def main():
    difficulties = ["Cheater", "Easy", "Normal", "Hard", "Ridiculous"]
    difficulty = input("""Choose your difficulty level:
Cheater
Easy
Normal
Hard
Ridiculous
> """)
    while difficulty not in difficulties:
        difficulty = random.choice(difficulties)
    if difficulty == "Cheater":
        incorrect_count = -999999999999992
    elif difficulty == "Easy":
        incorrect_count = -4
    elif difficulty == "Normal":
        incorrect_count = 0
    elif difficulty == "Hard":
        incorrect_count = 4
    elif difficulty == "Ridiculous":
        incorrect_count = 7

    clear_screen()
    secret_word = pick_secret_word()
    secret_word_length = len(secret_word)
    guess = "-" * secret_word_length
    letters_guessed = []
    bonus_letter = chr(random.randint(ord("a"), ord("z")))

    while incorrect_count < 8 and guess != secret_word:
        print("Difficulty: " + difficulty)
        print_clothesline(incorrect_count)
        print()
        # print("Bonus letter is: " + bonus_letter)  # for debugging
        print("Word:    " + guess)
        if letters_guessed == []:
            print("Guesses: " + " ".join(letters_guessed))
        else:
            if is_correct == True:
                print_green("Guesses: " + " ".join(letters_guessed))
            else:
                print_red("Guesses: " + " ".join(letters_guessed))
        print()
        letter = input("""Guess a letter...if you dare!
> """).strip(" ")
        while letter == "":
            letter = input("""Guess a letter...if you dare!
> """).strip(" ")
        letter = letter[0]
        incorrect_count = random_bonus(letter, bonus_letter, incorrect_count)
        letters_guessed.append(letter)
        is_correct = is_letter_in_word(letter, secret_word)
        clear_screen()
        if is_correct == True:
            guess = update_guess(guess, letter, secret_word)
        else:
            incorrect_count = incorrect_count + 1
        if letter == bonus_letter:
            print("You guessed the secret bonus letter! Have a one-time extra guess.")

    if incorrect_count == 8:
        print_clothesline(incorrect_count)
        print()
        print("Word:    " + guess)
        print_red("Guesses: " + " ".join(letters_guessed))
        print()
        print_red("The word was '" + secret_word +
                  "' -- you LOSE! Good DAY sir!")
    else:
        print_clothesline(incorrect_count)
        print()
        print("Word:    " + guess)
        print_green("Guesses: " + " ".join(letters_guessed))
        print()
        print_green("YOU WIN!!")


def random_bonus(letter, bonus_letter, incorrect_count):
    if letter == bonus_letter:
        incorrect_count = incorrect_count - 1
        return incorrect_count
    else:
        return incorrect_count

        # two issues. 1, "print" isn't showing up. 2, this can be abused by the user (doesn't disable after one use)

# old pick_secret_word function using a list manually populated by me

# def pick_secret_word():
#     secret_word_options = ["mother", "yeet", "brand", "leave", "director", "disagreement", "muscle", "harmful", "perceive", "necklace", "draft", "hay",
#                            "expect", "patent", "class", "convert", "cause", "patient", "looting", "mechanical", "neck", "scratch", "spray", "field", "likely", "company"]
#     random_secret_word = random.choice(secret_word_options)
#     return random_secret_word


def pick_secret_word():
    secret_word_options = []
    # f = open("easy_words.txt", "r") # this directly open easy_words.txt
    # this opens the file specified in the command line
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    for line in lines:
        secret_word_options.append(line.strip())
    random_secret_word = random.choice(secret_word_options)
    return random_secret_word


# Alternative code for pick_secret_word function:
# def pick_word():
#     word_filename = "easy_words.txt"
#     word_file = open(word_filename)
#     all_text = word_file.read()
#     all_words = all_text.splitlines()
#     word_file.close()

#     word = random.choice(all_words)
#     return word


def clear_screen():
    print("\033[H\033[J", end="")


def is_letter_in_word(letter, word):
    if letter in word:
        return True


def print_clothesline(incorrect_count):
    if incorrect_count <= 0:
        print_green(image1)
    elif incorrect_count == 1:
        print_green(image2)
    elif incorrect_count == 2:
        print_green(image3)
    elif incorrect_count == 3:
        print_yellow(image4)
    elif incorrect_count == 4:
        print_yellow(image5)
    elif incorrect_count == 5:
        print_yellow(image6)
    elif incorrect_count == 6:
        print_red(image7)
    elif incorrect_count == 7:
        print_red(image8)
    elif incorrect_count == 8:
        print_red(image9)
    print("Number of incorrect guesses left: " + str(8 - incorrect_count))


def update_guess(old_guess, letter, secret_word):  # this one is a doozy!
    new_guess = ""
    for index in range(len(old_guess)):
        if secret_word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]

    return new_guess


# this is Matt's breakdown of what is happening in the above update_guess function.

# guess = "_____"
# word = "apple"  # [a,p,p,l,e]
# letter1 = "a"
# letter2 = "l"
# letter3 = "e"
# letter4 = "z"


# def update_guess(old_guess, letter,  word):
#     input("old guess: " + old_guess)
#     input("letter: " + letter)
#     new_guess = ""                 # [a,p,p,l,e]
#     for index in range(len(word)):  # [0,1,2,3,4]
#         input("word index: " + word[index])
#         if word[index] == letter:
#             new_guess = new_guess + letter
#             input("new guess: " + new_guess)
#         else:
#             new_guess = new_guess + old_guess[index]
#             input("new guess: " + new_guess)

#     print()
#     return new_guess


# guess = update_guess(guess, letter1, word)
# guess = update_guess(guess, letter2, word)
# guess = update_guess(guess, letter3, word)
# guess = update_guess(guess, letter4, word)

def print_red(msg):
    print("\033[0;30;41m" + msg + "\033[0;0m")


def print_yellow(msg):
    print("\033[0;30;43m" + msg + "\033[0;0m")


def print_green(msg):
    print("\033[0;30;42m" + msg + "\033[0;0m")

# All 9 ASCII images


image1 = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""

image2 = r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""

image3 = r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````
"""

image4 = r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
"""

image5 = r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

image6 = r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""

image7 = r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

image8 = r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""

image9 = r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
"""

# runs the program

clear_screen()

main()
