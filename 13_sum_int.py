A = int (input(" pleas entre number to clacule the sum of the int :"))

while A <= 1:
    A = int(input("entry number"))
    
S = 0
i = 1

while i <= A:
    S = S + i
    i = i + 1
    
print(" the sum is :", S)