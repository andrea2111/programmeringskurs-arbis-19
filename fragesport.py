def check_answer(guess, answer):

    if guess.lower() == answer.lower():
        global points
        
        points += 1
        print ("Rätt!")
    else:
        print ("Fel!")

points = 0

print('Svara alltid "Ja" eller "Nej"')

svar_1 = input('Är Niinistö Finlands president? ')
check_answer(svar_1, 'ja')

svar_2 = input('Är jorden rund? ')
check_answer(svar_2, 'ja')

svar_3 = input('Är ett dygn 25 timmar? ')
check_answer(svar_3, 'nej') 

print ('Du fick ' + str(points) + ' poäng!')