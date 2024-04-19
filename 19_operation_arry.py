





#concatenation
L1 = L[2,4,7,9]
L2 = L[15,4,7,0]

L = L1 + L2


#repetition

L = L[3,4,5]
L = L * 3

#comparison

L1 = L[3,4,6]

L2 = L[3,5,7]

print( L1 >= L2 )



# affectation - Decoupage
L['Ali' , -6 , 10 , 2.5, 'd', True]


#===> Remplacer les 3 premier elements
L[:3] = [23 , 'Anis' , 8.36]


#===> Remplacer les 2 dernier element
L[-2:] = ['c', False]


#===> Remplacer 3 element par 2 elements
L[1:4] = ['ok' , True] 


#===> Remplacer 1 element par 3 element
L[1:2] = ['Beau' , -8.36 , 'Vol']


#===> Remplacer les2 element par 0 elements
L[3:5] = [ ]


#===> Ajouter 2 elements
L[-2:-2] = [0,'USA']


#===> Ajouter 1 a la fin de la liste 
L[50:] = ['Fin']


#===> Remplacer les element dont l'indice impair
L[0::2] = [8,False,4,'Info']


#===> Remplacer les elment 1 , 4 , 7 par 1 element 
L[1::3] = [8]#Erreur


#===> Remplacer toute la liste par une nouvelle
L[:] = [10 , 20 , 30]