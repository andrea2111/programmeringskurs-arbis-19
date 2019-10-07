
class Katt:
    def __init__(self, name, age, color, candy):
        self.name = name 
        self.age = age
        self.color = color
        self.candy = candy

mina_katter = []

while True:
    print ()
    action = input("Vill du se en lista på katter (A), lägga till en ny katt (B) eller avsluta (C)? ")
    print ()
    if action.upper() == "C":
        break
    elif action.upper() == "B":
        name = input("Vad heter katten? ")
        age = input("Hur gammal är katten? ")
        color = input("Vilken färg är katten? ")
        candy = input("Vad är kattens favoritgodis? ")
        min_katt = Katt(name, age, color, candy)
        mina_katter.append(min_katt)
    elif action.upper() == "A":
        for katt in mina_katter:
            print (katt.name, katt.age, katt.color, katt.candy)
            print ()
    else:
        print ("Försök igen!")
    