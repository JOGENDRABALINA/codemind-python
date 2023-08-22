'''Array: Collection of homogeneous type of elements.

Core data types: collection of heterogenous type of elements.

list,set,tuple,dictionary (replacement of arrays in python).
Array : Collection of homogeneous type oh elements.

Core data types : Collection of heterogeneous type oh elements.

list,set,tuple,dictionary (replacement of arrays in python)

INBUILT FUNCTIONS -->LISTS
--------------------------
list : a=[1,2,3,4] (in python if we take square braces it inbuilt take as an array)
       a=[1,0.2,True,'Hi'] (this is also a list)
       len (a) (it is used to find the length of array)
       max(a) (to find maximum number in list)
       min(a) (to find minimum number in list)
       
Declaration : a=list(map(int,input().split())) (to read inputs)
  Accessing Elements : Through index values we can access the elements in python like C and it has also negative index
                       starting from -1 but from reverse.
                       EG: a=[10,20,30]
                       accessing : a[1]=10 a[2]=20 or a[-3]=10 a[-2]=20 a[-1]=30
  Accessing two elements or more elements at a time : a[stating element index: ending+1:step size]
                                                      EG: a[1:3] = [10,20] or a[-3:-1]= [10,20]
                                                      a[:],a[::],a[::1],a[0::1] (These all are same)

  IMPOTANT FUNCTIONS IN PYTHON: a.append(number)-->It will insert the number at the end.
    (MODIFY)                    a.insert(index,number)-->Through this we can insert an element wherever we want.
                                a[index]=number -->Modify the existing element.
                                a.index(number) -->To find the index number of the element.
                                                   If we have same elements and we ask the index it will give the 1st element index.
                                a.sort() -->It will make the elements sorted in ascending order.
                                a.sort(reverse=True) -->It will make the elements sorted in descending order.
                                sorted(a) -->The array or list is Sorted in ascending order but it dont disturb the original array.
                                sorted(a,reverse=True) -->The array or list is Sorted in descending order but it dont disturb the original array.
                                a.pop() -->It delete the last element (quitely opposite to append)
                                a.pop(index) -->To delete a particular element present in the index.
                                del a[index] -->same as pop but it directly delete the element and print the list but pop print the delete element.
                                del a[from index:to index+1] -->To delete more than one element.
                                a.remove(number in the list) -->without using index directly deleting the element.
                                a=[1,4,2] b=a b=[1,4,2] but a.pop() if we print a=[1,4] and b=[1,4].Here b also effected due to same memory location.
                                b=a.copy() -->The values of copied in b in different memory location.
                                             EG :  a=[1,2,3,4,5]
                                                    b=a.copy()
                                                    a.pop()
                                                    5
                                                    a
                                                    [1, 2, 3, 4]
                                                    b
                                                    [1, 2, 3, 4, 5]
                                del a --> delete the entire list.
                                del a[:] or a.clear() -->delete the elements in the list and makes the list empty we can add the elements if we want.
                                a.append([number,number]) -->Not possible to add two numbers it take it as sublist.
                                a.extend([number,number]) -->It is possible to join two or more elements at a time in list.  

a=[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
a.append(10)
a
[1, 2, 3, 4, 5, 10]
a.insert(2,90)
a
[1, 2, 90, 3, 4, 5, 10]
a[3]=324
a
[1, 2, 90, 324, 4, 5, 10]
a.index(1)
0
a.index(5)
5
max(a)
324
min(a)
1
a.sort()
a
[1, 2, 4, 5, 10, 90, 324]
sorted(a)
[1, 2, 4, 5, 10, 90, 324]
a
[1, 2, 4, 5, 10, 90, 324]

a=list(map(int,input().split()))
print(max(a))

method to run a loop on index
a=[3,5,2,5,3,6]
for i in range(0,len(a)):
    print(i,a[i])
 
OUTPUT:
    0 3
    1 5
    2 2
    3 5
    4 3
    5 6

printing even numbers in list
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if a[i]%2==0:
        print(i,a[i])

another method to run a loop directly on element
a=list(map(int,input().split()))
for i in a:
    print(i)

Finding Maximum number without using inbuilt function
a=list(map(int,input().split()))
max=0
for i in a:
    if i>max:
        max=i
print(max)

DICTIONARY
-----------
Declaration : a={key:value,key:value,.....} -->(Key can be alphabet or number)
             EG : a={'s1':34,'s2':87,'s3':98},a={1:34,2:87,3:98}
Accessing : a[key]
           a['s1']=34
Length : len(a)=3
         a={'s1':[34,21,34],'s2':[12,3,43]}
Maximum in dictionary : max(a[key])
Average : sum(a[key])/len(a[key])
a.keys() : print keys.
a.values() :print values.
a.items() :print both keys and values.

           EG:  a={1:33,2:32,3:54}
                a.keys()
                dict_keys([1, 2, 3])
                a.values()
                dict_values([33, 32, 54])
                a.items()
                dict_items([(1, 33), (2, 32), (3, 54)])'''

##printing maximum number
##a=[10,20,30,40,50]
##print('The maximum number is: ',max(a))

##printing minimum number
##a=[10,20,30,40,50]
##print('The maximum number is: ',min(a))

##printing length of the list
##a=[10,20,30,40,50]
##print('The length of the list is: ',len(a))

##printing all data types in a same list
##a=[0.3,28,2003,'JOGENDRA',True]
##print(a)

##giving values by custamised input
##a=list(map(int,input('Enter the list: ').split()))
##print('The maximum number is: ',max(a))
##print('The minimum number is: ',min(a))
##print('The length of the list is: ',len(a))

##printing index position
##a=[10,20,30,40,50]
##print(a[1])
##
####printing index position
##a=[10,20,30,40,50]
##print(a[1:3])
##
####printing index position
##a=[10,20,30,40,50]
##print(a[:])
####output:
##[10, 20, 30, 40, 50]
##
####printing index position
##a=[10,20,30,40,50]
##print(a[: :])
####output:
##[10, 20, 30, 40, 50]
##
####printing index position
##a=[10,20,30,40,50]
##print(a[: : ])
####output:
##[10, 20, 30, 40, 50]
##
####printing index position
##a=[10,20,30,40,50]
##print(a[: : 2])
####output:
##
####printing index position
##a=[10,20,30,40,50]
##print(a[-4:-1])
####output:
##
####printing index position
##a=[10,20,30,40,50]
##print(a[: : 2])
####output:
##
####printing index position
##a=[10,20,30,40,50]
##print(a[-1])
####output:

##Inserting element at the end
##a=[1,5,4,3,2]
##a.append(6)
##print(a)

##Inserting element at the middle or which we want
##a=[5,7,8,6,3,2]
##a.insert(1,6)
##print(a)
##output:
##[5, 6, 7, 8, 6, 3, 2]

##Index position
##a=[5,3,8,6,3,2]
##print(a.index(3))
##output:
## 1

##sorting
##a=[30,50,44,23,67,89]
##a.sort()
##print(a)
##output:
##[23, 30, 44, 50, 67, 89]

##sorting in reverse
##a=[30,50,44,23,67,89]
##a.sort(reverse=True)
##print(a)
####output
##[89, 67, 50, 44, 30, 23]

##sorting
##a=[30,50,44,23,67,89]
##print(sorted(a))
####output:
##[23, 30, 44, 50, 67, 89]

##pop the element delete the last element
##a=[1,2,3,4,5,6]
##a.pop(5)
##print(a)
####output
##[1, 2, 3, 4, 5]

##delete element
##a=[7,8,3,4,9,2,6]
##del a[1]
##print(a)
####output:
##[7, 3, 4, 9, 2, 6]

##delete element
##a=[7,8,3,4,9,2,6]
##del a[1:3]
##print(a)
##output:
##[7, 4, 9, 2, 6]

##pop the element delete the last element
##a=[1,2,3,4,5,6]
##a.pop(3)
##print(a)
####output
##[1, 2, 3, 5, 6]

##pop the element
##a=[2,5,8]
##b=a
##a.pop()
##print(a)
##print(b)
##output:
##[2, 5]
##[2, 5]

##pop the element with out effect another value
##a=[2,5,8]
##b=a.copy()
##a.pop()
##print(a)
##print(b)
##output:
##[2, 5]
##[2, 5, 8]

##delete the entire list
##a=[2,5,8,7,43,89]
##del a[:]
##print(a)
##output:
##[]

##clear the entire list
##a=[2,5,8,7,43,89]
##a.clear()
##print(a)
####output:
##[]

##Appen the elements in last
##a=[3,6,8,7,4,3,2]
##a.append([2,3,4])
##print(a)
##output
##[3, 6, 8, 7, 4, 3, 2, [2, 3, 4]]

##Extend the list adding multiple numbers
##a=[3,6,8,7,4,3,2]
##a.extend([2,3,4])
##print(a)
##output:
##[3, 6, 8, 7, 4, 3, 2, 2, 3, 4]

##printing the index values
##a=[4,7,6,5,4,3]
##for i in range(0,len(a)):
##    print(i,end=' ')
##output:
##0 1 2 3 4 5 

##printing the index values
##a=[4,7,6,5,4,3]
##for i in range(0,len(a)):
##    print(i,a[i])
##output:
##0 4
##1 7
##2 6
##3 5
##4 4
##5 3

##printing the index values
##a=[10,20,30,40,50]
##for i in range(0,len(a)):
##    print(i,'-->',a[i],end=' ')
##output:
##0 --> 10 1 --> 20 2 --> 30 3 --> 40 4 --> 50

##printing Even numbers in a list
##a=list(map(int,input('Enter the list: ').split()))
##for i in range(0,len(a)):
##    if a[i]%2==0:
##        print(a[i])
##output:
##    2,8,4

##printing numbers in a list second method 2
##a=list(map(int,input('Enter the list: ').split()))
##for i in a:
##        print(i,end=' ')
##output:
##1 2 3 4 5

##printing maximum element without using max keyword
##a=list(map(int,input('Enter the list: ').split()))
##m=0
##for i in a:
##    if i>m:
##        m=i
##print('The maximum number is: ',m)
##ouput:
##Enter the list: 10 20 30 40 50
##The maximum number is: 50




















































