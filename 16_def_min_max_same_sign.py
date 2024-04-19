def Same_sign( A , B ):
    if A * B > 0:
        print("the two number has the same sign")
    else:
        print("the two number has difrent sign")


def Minimum(A , B):

    if A > B:
        return A
    else:
        return B

def Maximun( A , B):
    
    if A < B:
        return B
    else:
        return A
    
    
#call the function
    
A = float( input( "Pleas entry the first number:"))
B = float( input( "Pleas entry the Second number:"))

Same_sign( A , B )
print("the minimuml value is : ", Minimum(A , B))
c = Maximun(A , B)
print("the maximuml value is : ", Maximun(A , B))