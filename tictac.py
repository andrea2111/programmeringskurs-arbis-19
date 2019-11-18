field = ["-", "-","-", "-","-", "-","-", "-","-"]

def draw_field():
  print(field[:3])
  print(field[3:6])
  print(field[6:])

def update_field(symbol, position):
  if field[position] == "-":
    field[position] = symbol
  else:
    print()
    print("Där kan du inte lägga din symbol! Försök igen!")
    print()

while True:
  draw_field()
  print()
  if not "-" in field:
    print("Spelet är över!")
    break
  else:
    symbol = input("X eller O? ").upper()
    position = int(input("Var vill du rita din symbol? (Plats 0-8) "))
    print()
    if (symbol == "X" or symbol == "O") and position < 9:
      update_field(symbol, position)
    else:
      print()
      print("Försök igen!")
      print()