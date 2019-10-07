import random

print ("Welcome to Hangman!")

wordlist = ["apple", "house", "python", "download", "secret"]
word = random.choice(wordlist)

turns = 10
guesses = ""

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print (char, )
        else:
            print ("_", )
            failed += 1
    if failed == 0:
        print ("You won!")
        print ()
        break
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("Wrong!")
        print ("You have ", turns, " more guesses!")
        print ()
    if turns == 0:
        print ("You lose!")
        print ()
