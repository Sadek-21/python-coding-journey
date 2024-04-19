print(" Programme qui afficher la somme des 20 premiers entiers positifs :")
N = int ( input ( " Veuillez saisir un nomber :"))

S = 0
for i in range( 1 , N + 1 ):
    S = S + i 
    
print("La somme des 20 premiers entiers positifs est :" , S)