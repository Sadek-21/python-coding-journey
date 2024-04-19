


L1 = [10 ,2 ,3,4,5,8,5,0,3,34,34,]
L4 = ['Python' , 'c++' , 'Java' , 'PHP' , 'C#']


L2 = sorted(L1)
print(L2)

L3 = sorted(L1 , reverse = True)
print(L3)

L5 = sorted(L4,key=str.lower)
print(L5)

L6 = sorted(L4 , key=str.lower , reverse = True)
print(L6)

L7 = sorted(L4 , key=len , reverse = True)
print(L7)