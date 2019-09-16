points = 0

print('Svara alltid "Ja" eller "Nej"')

svar_1 = input('Är Niinistö Finlands president? ')

if svar_1.lower() == 'ja':
    points += 1
elif svar_1.lower() == 'nej':
    points -= 1
else:
    print('Svara alltid "Ja" eller "Nej"')

svar_2 = input('Är jorden rund? ')

if svar_2.lower() == 'ja':
    points += 1
elif svar_2.lower() == 'nej':
    points -= 1
else:
    print('Svara alltid "Ja" eller "Nej"')

svar_3 = input('Är ett dygn 25 timmar? ')

if svar_3.lower() == 'ja':
    points -= 1
elif svar_3.lower() == 'nej':
    points += 1
else:
    print('Svara alltid "Ja" eller "Nej"')

print ('Du fick ' + str(points) + ' poäng!')