
P = ['Maroc' , 'Algerie' , 'Tunisie' , 'Mali' , 'France']

 
P1 = input('entry the first country :')

P2 = input('entry the second country :')

i = P.index(P1)
j = P.index(P2)

P[i] , P[j] = P[j] , P[i]

print(P)