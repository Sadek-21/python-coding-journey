L = [ 10 , 15 , -6 , 2]

print(L)   # Afficher tout les element

print(L[0]) # Afficher du premier elment

L[1] = 3  # Modifivation de la valeur
print(L)

print(L[-1])  #Indexage negative

#EX1
lettre = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W,''X','Y','Z' ,' ']

print(lettre)

print(lettre[12],lettre[14],lettre[7],lettre[0],lettre[12],lettre[4],lettre[3], lettre[-1],lettre[18],lettre[0],lettre[3],lettre[4],lettre[10],sep = '')


#EX2

Days = ["Lundi","Mardi","Mercredi","jeudi","vendredi","Samedi","Dimanche"]

print("Le premier jour de la seaine est :",Days[0])
print("Le premier jour de la seaine est :",Days[-7])
print("Le deux jours de week end sont",Days[5],Days[6])
print("Le deux jours de week end sont",Days[-2],Days[-1])
print("les trois premiers jours de la semaine sont :",Days[0],Days[1],Days[2])
print("les trois premiers jours de la semaine sont :",Days[-7],Days[-6],Days[-5])

#Ex3

N = int(input("Pleas entry number positive : "))

while N < 1:
    N = int(input("Pleas entry number positive : "))
    
L = list(range(1,N+1))

print(L)

L1 = list(range(0,N+1,2))

print(L1)

L2 = list(range(1,N+1,2))

print(L2)



print(Days[::-1])

print(Days[1:-3])


