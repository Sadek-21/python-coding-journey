import random

secretnumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print('Take a guesse')
    guess = int(input())

    if guess < secretnumber:
        print('Your guesse is too low.')
    elif guess > secretnumber:
        print('Your guesse is too high')
    else:
        break

if guess == secretnumber:
    print('Good job! You guessed my number in ' +str(gussesTaken) + 'Guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber))
        
