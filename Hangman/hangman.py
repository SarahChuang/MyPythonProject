"""
File: hangman.py
Name: Han Hsiu
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays a hangman game.
    Players can input an alphabet to guess the word.
    Players have N_TURNS chances to try and win this game.
    """
    answer = random_word()
    answer1 = answer
    dashed = ""
    ans = ""
    life = N_TURNS
    for j in range(len(answer)):
        dashed += "-"
    while life > 0:
        print("The word looks like: " + dashed)
        print("You have " + str(life) + " wrong guesses left.")
        input_ch = input("Your guess: ").upper()
        if input_ch.isalpha():
            if len(input_ch) == 1:
                k = answer1.find(input_ch)
                if k == -1:
                    life -= 1
                    print("There is no " + input_ch + "'s" + " in the word.")
                    ans += dashed
                else:
                    print("You are correct!")
                    while k != -1:
                        dashed = replace(dashed, k, input_ch)
                        answer1 = replace(answer1, k, "-")
                        k = answer1.find(input_ch)
            else:
                print("illegal format.")
        else:
            print("illegal format.")
        if dashed == answer:
            print("You win!!")
            break
    if life == 0:
        print("You are completely hung :(")
    print("The answer is: " + answer)


def replace(a, b, c):
    """
    :param a: str, random word
    :param b: int, position of the word
    :param c: str, alphabet of the specific position of the word
    :return: str, answer of the game
    """
    s = a[:b]
    s += c
    s += a[b + 1:]
    return s


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
