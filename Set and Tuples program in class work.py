'''Tuple: immutable'''

##printing elements in tuple
##a=(1,2,3,4)
##print(a)
##output:
##(1,2,3,4)

##printing element indexes in tuple
##a=(1,2,3,4)
##print(a[1])
##output:
##2

'''Sets: unordered list,without duplicates'''
##printing lenghth in set
##a={2,1,4,3,2,1}
##print(len(a))
##output:
##4 '''Duplicate values are not allowed in set'''

##printing
##a={8,1,1,4}
##print(a)
##output:
##{8, 1, 4}

##Adding the element
##a={8,1,1,4}
##a.add(5)
##print(a)
##output:
##{8, 1, 4, 5}

##deleting the element
##a={8,1,1,4}
##a.remove(4)
##print(a)
##output:
##{8, 1}

##printing
##a=[9,0]
##b=set(a)
##c=tuple(a)
##d=list(a)
##print(a,b,c,d)
##output:
##[9, 0] {0, 9} (9, 0) [9, 0]

##printing
##a=[1,1,1,2,3,2,3]
##b=[]
##for i in a:
##    if i not in b:
##        b.append(i)
##print(b)
##print(list(set(a)))
##output:        
##[1, 2, 3]
##[1, 2, 3]























