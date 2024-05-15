
N = [12,34,13,65,23,7,1,613,41,12,15,17,131,12,7,9,1,0,3,7,2,9,2,8,12,12,34,13,65,23,7,1,613,41,12,15,17,131,12,7,9,1,0,3,7,2,9,2,8,12]


for note in N :
    print(note)
    

for i in range(len(N)) :
    print("La note de l'etudiant num",i+1,"est:",N[i])
    
    
infos = ['Anas' , 'Radi' , 2000 , 'France' , 'Paris']

for valeur in infos :
    print(valeur)
    

for i in range(len(infos)) :
    print('infos[',i+1,']=',infos[i])
    
    
    
    
for i , note in enumerate(N):
    print("La note de l'etudiant num", i+1 , "est:", note)
    
    

for i , note in enumerate(N , start=1):
    print("La note de l'etudiant num", i , "est:", note)
 
 
 
L = ['C#' , 'C++' , 'JAVA' , 'PHP' , 'Python']
D = [2000 , 1980 , 1995 , 1994 , 1991]
C = ['Microsoft' , 'Bjarne Stroustrup' , 'Sun Microsystems' , "Ramus Lerdorf" , 'Guido van Rossum']

for L , D , C in zip  ( L , D , C ):
    print( L , 'est cree en ' , D , 'par' , C)
    
    
    
    
    
notes = []

for i in range(5) :
    print("Donner la note de letudiant num" , i+1, ":", end=" ")
    notes.append(float(input()))
    


for i , v in enumerate(notes , 1):
    print("La note de letudiant num", i , "est:" , v)
    








X = int(input("Ente la valeur de x :"))

L = []
for i in range(5) :
    print('L[',i+1,']=' , end=' ')
    L.append(int(input()))
if X in L:
    print(X, 'se trouve dans L')
else:
    print(X, 'ne se trouve pas dans L')
