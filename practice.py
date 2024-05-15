import random

def collatz(number):

    if number % 2 == 0:
        return number // 2
    else:
        return (3*number) + 1



N = int(input('Pleas entry a number '))

print(collatz(N))
    
