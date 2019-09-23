katalog = {'anna': 'anna@example.com', 'emil': 'emil@example.com', 'petra': 'petra@example.com'}

print('Hej och välkomment till e-postkatalogen!')

def soka():
    soka_namn = input('Vem vill du söka efter? ').lower()
    if soka_namn in katalog:
        print(katalog[soka_namn])
    else:
        print(soka_namn + ' finns inte i katalogen.')
    start()

def lagg_till():
    namn = input('Skriv in namnet: ').lower()
    epost = input('Skriv in e-posten: ').lower()
    katalog[namn] = epost
    print('Lade till ' + namn + ': ' + epost)
    start()

def start():
    svar = input('Vill du söka efter en adress eller lägga till en ny? Svara "S" för att söka och "L" för att lägga till. ').lower()
    if svar == 's':
        soka()
    elif svar == 'l':
        lagg_till()

start()
