##d={'s1': 34,'s2': 66,'s3': 98,}
##print(d['s1'])
##output:
##34

##printing
##d={'s1': [45,6,23],'s2': [78,98,4],'s3': [65,78,34],}
##print(d['s1'])
##output:
##[45, 6, 23]

##printing length of a dictionary
##a={1:2,3:4,5:6}
##print(len(a))
##output:
##3

##printing updating or adding values 
##a={4:5,6:9,5:3,1:1}
##a.update({2:3,8:7,7:4})
##print(a)
##output:
##{4: 5, 6: 9, 5: 3, 1: 1, 2: 3, 8: 7, 7: 4}

##Delete the element
##a={4:5,6:9,5:3,1:1}
##del a[1]
##print(a)
##ouput:
##{4: 5, 6: 9, 5: 3}

##------------------------------------------------------>loops running in dictonaries
##loops---------------------------------->Best method
##a={4:5,6:9,5:3,1:1}
##for i in a.keys():
##    print(i,a[i])
##output:
##4 5
##6 9
##5 3
##1 1

##loops
##a={4:5,6:9,5:3,1:1}
##for i in a.values():
##    print(i)
##output:
##5
##9
##3
##1

##loops------------------------------>2nd best method
##a={4:5,6:9,5:3,1:1}
##for i,j in a.items():
##    print(i,j)
##output:
##4 5
##6 9
##5 3
##1 1

##How many times the same number is repeated
##a=[1,2,3,1,5,4,3,3,1,2,4,7]
##d={}
##for i in a:
##    if i not in d.keys():
##        d[i]=1
##    else:
##        d[i]+=1
##print(d)
##output:
##{1: 3, 2: 2, 3: 3, 5: 1, 4: 2, 7: 1}

##printing same list two times
##a=[2,3,1,3,4,213]
##print(a+a)
##output:
##[2, 3, 1, 3, 4, 213, 2, 3, 1, 3, 4, 213]














































































































