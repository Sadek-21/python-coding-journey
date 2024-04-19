Analyse = [ 10 , 12 , 14.5 , 6 , 2,5]
Algebre = [ 8 , 6,5 , 12 , 14.5 , 10.5]
Probabilite = [ 9.5 , 14 , 12 , 15 , 13.5]
Statistique = [ 19 , 20 , 10 , 19 , 18]


S = sum(Analyse + Algebre + Probabilite + Statistique)
M = S / len(Analyse + Algebre + Statistique + Probabilite)
Max = max(Analyse + Algebre + Probabilite + Statistique)
Min = min(Analyse + Algebre + Probabilite + Statistique)


print('La Somme des notes est :' , format(S , '.2f'))
print('La Moyenne des notes est :',format(M , '.2f'))
print('La Note Maximale des notes est :',format(Max , '.2f'))
print('La Note Minimale des notes est :',format(Min , '.2f'))
