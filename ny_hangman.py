import random

words = ["house", "blaze", "jelly", "check"]

clue = ["?", "?", "?", "?", "?"]

lives = 7

correct_word = random.choice(words)

print("Här är det hemliga ordet: ")

def check_guess(guess, correct_word, clue):
  global lives
  if guess not in correct_word:
    print()
    print("Fel!")
    lives -= 1
  elif guess in correct_word:
    print()
    print("Rätt!")
    for i in range(len(correct_word)):
      if correct_word[i] == guess:
        clue[i] = guess
  

while True:
  print(clue)
  print("Du har " + str(lives) + " försök kvar.")
  print()
  if "?" not in clue:
    print("Du vann!")
    break
  guess = input("Gissa en bokstav: ").lower()
  check_guess(guess, correct_word, clue)
  if lives == 0:
    print("Du förlorade!")
    break