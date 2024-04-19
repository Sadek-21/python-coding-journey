
L1 = [10 ,2 ,3,4,5,8,5,0,3,34,34,]
L2 = ['Python' , 'c++' , 'Java' , 'PHP' , 'C#']

L1.sort()
print(L1)

L1.sort(reverse = True)
print(L1)



L2.sort(key=str.upper) # ou L2.sort(key=str.lower)
print(L2)

L2.sort(key=str.upper , reverse = True)
print(L2)

L2.sort(key=len , reverse = True)
print(L2)


