S = 0 
for i in range( 8 ):
    print( "pleas entry number ", i + 1 ,":" , end="")
    X = int ( input())
    if X < 0 :
        break
    S = S + X 
    
print("The sum for this number is :",S)

