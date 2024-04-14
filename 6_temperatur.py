print(" Programme qui determine l'etat de l'eau :")
Temp = float( input( " Veuillez saisir la valeur de tempurature :"))

if Temp <= 0 :
    print (" l'eau et dans letat GLACE ")
elif  Temp < 100:
    print (" l'eau et dans letat LIQUIDE ")
else :
    print (" l'eau et dans letat VAPEUR ")