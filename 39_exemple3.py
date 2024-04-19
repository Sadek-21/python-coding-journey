#palindrom

mot = input("entry the name : ")
L = list(mot)

P = L.copy()

L.reverse()

print(L)
print(P)

if L == P :
    print(mot,"est un mot palindrom")
else:
    print(mot,"est un mot non palindrom")
 