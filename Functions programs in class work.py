##Function example
##def sample():
##    print(2003)
##sample()
##output
##2003

##Function example
##def sample():
##    print(2003)
##sample()
##print('JOGENDRA')
##sample()
##output
##2003
##JOGENDRA
##2003

##Function example
##def sample():
##    print('Name: JOGENDRA')
##    print('COllege: Aditya college')
##sample()
##print('Roll No: 22MH1A05F9')
##print('Branch: CSE')
##output
##Name: JOGENDRA
##COllege: Aditya college
##Roll No: 22MH1A05F9
##Branch: CSE

##addition
##a,b=map(int,input().split())
##def sample(a,b):
##    print(a+b)
##sample(a,b)
##sample(10,10)
##sample(50,50)
##output
##5 5
##10
##20
##100

##printing calculator---------------->calculator
##a=int(input('Enter the number: '))
##b=int(input('Enter the number: '))
##print('press 1 for Addition')
##print('press 2 for Substraction')
##print('press 3 for Multliplication')
##print('press 4 for Division')
##print('press 5 for Modulo')
##print('press 6 for Power')
##c=int(input('choose any number from 1 to 6: '))
##def sample(a,b):
##    if c==1:
##        print(a+b)
##    elif c==2:
##        print(a-b)
##    elif c==3:
##        print(a*b)
##    elif c==4:
##        print(a/b)
##    elif c==5:
##        print(a%b)
##    elif c==6:
##        print(a**b)
##    else:
##        print('chi poora')
##print('The correct solution is: ')
##sample(a,b)
##output
##Enter the number: 10
##Enter the number: 10
##press 1 for Addition
##press 2 for Substraction
##press 3 for Multliplication
##press 4 for Division
##press 5 for Modulo
##press 6 for Power
##choose any number from 1 to 6: 1
##The correct solution is: 
##20

##My program
##print('press 1 for Jogendra')
##print('press 2 for srinivas')
##print('press 3 for bharathwaj')
##print('press 4 for Rajesh')
##print('press 5 for Deepu')
##print('press 6 for Abhishek')
##c=int(input('choose any number from 1 to 6: '))
##if c==1:
##    print('Jogendra is Honest and simplicity')
##elif c==2:
##    print('srinivas is tetoolar and dancer')
##elif c==3:
##    print('bharathwaj is moodist and drunken')
##elif c==4:
##    print('Rajesh is Alage and Topper of CSE')
##elif c==5:
##    print('Deepu is kinded and Richest')
##elif c==6:
##    print('Abhishek is hurted and insta reel star')
##out put
##press 1 for Jogendra
##press 2 for srinivas
##press 3 for bharathwaj
##press 4 for Rajesh
##press 5 for Deepu
##press 6 for Abhishek
##choose any number from 1 to 6: 1
##Jogendra is Honest and simplicity

##printing calculator using function-------------------------->function
##def add(a,b):
##    print(a+b)
##def sub(a,b):
##    print(a-b)
##def mul(a,b):
##    print(a*b)
##def div(a,b):
##    print(a//b)
##a,b=map(int,input().split())
##c=int(input('Enter choice(1,2,3,4): '))
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##elif c==4:
##    div(a,b)
##else:
##    print('Wrong input')

##printing odd even using function
##def sample(a):
##    if a%2==0:
##        print(a,'is Even number')
##    else:
##        print(a,'is Odd number')
##a=int(input('Enter the number: '))
##sample(a)

##printing odd even using function----------->method 2
##def sample(n):#formal parameters
##    if n%2==0:
##        print(n,'is Even number')
##    else:
##        print(n,'is Odd number')
##a=int(input('Enter the number: '))#actual parameters
##sample(a)

##proper way of usinf function---------------------------------------------->proper way function
##def sample(n):
##    if n%2==0:
##        return('Even number')
##    else:
##        return('Odd number')
##a=int(input('Enter the number: '))
##x=sample(a)
##print(x)

##MEGA prime number program using while loop---------->mega prime
##n=int(input("Enter the number: "))
##for i in range(2,n):
##        if n%i==0:
##            print('NoT a Prime')
##            break
##else:
##    s=True
##    while n>0:
##         r=n%10
##         n//=10
##         for j in range(2,r):
##             if r%j==0:
##                s=False
##                break
##         else:
##             s=True
##             print(r)
##         if s==False or r==1:
##              print('Not a Mega prime')
##              break
##    if s==True and r!=1:
##        print('Mega prime')

##mega prime using function------------------------------>mega prime function
##def prime(n):
##    for i in range(2,n//2+1):
##        if n%i==0:
##            print('Not a mega prime')
##            break
##    else:
##         return(True)
##a=int(input('Enter the number: '))
##if prime(a):
##    s=1
##    while a>0:
##        rem=a%10
##        if prime(rem):
##            s=1
##        a//=10
##    if s:
##        print('Mega prime')
    
##Even and odd
##def sam():
##    for i in range(3):
##        n=int(input('Enter the number: '))
##        if n%2==0:
##            print('Even')
##        else:
##            print('Odd')
##sam()

##addition
##def sap():
##    a=int(input('Enter the number: '))
##    b=int(input('Enter the number: '))
##    c=a+b
##    print(c)
##sap()

##logic of function
##def sample(a):
##    print(a)
##    a=10
##    print(a)
##a=1
##sample(a)

##logic of function
##def sample(a):
##    print('first Inside a',a)
##    a=10
##    print('Inside a',a)
##a=1
##sample(a)
##print(a,'outside',a)
##output:
##first Inside a 1
##Inside a 10
##1 outside 1

##logic of function
##def sample(a):
##    print('Inside1',a)
##    a=20
##    print('Inside2',a)
##a=10
##a=20
##a=30
##c=60
##sample(a)
##print(c,'outside',a)
##output
##Inside1 30
##Inside2 20
##60 outside 30

##logic 
##def jog():
##    a=20
##    b=50
##    print(a+b)
##a=5
##b=10
##jog()
##print('sub:',a-b,'mul:',a*b,'add:',a+b,'div:',a/b)
##output
##70
##sub: -5 mul: 50 add: 15 div: 0.5

####function
##def jog():
##     a=int(input('Enter the number a: '))
##     b=int(input('Enter the number b: '))
##     if a<b:
##         print('a is bigger')
##     else:
##         print('b is bigger')
##def gen():
##     n=int(input('Enter the number: '))
##     if n%2==0:
##         print('Even')
##     else:
##         print('Odd')
##a=50
##jog()
##gen()
##print(a)
##output
##Enter the number a: 20
##Enter the number b: 30
##a is bigger
##Enter the number: 2
##Even
##50

##logic
##a=int(input('Enter the number a: '))
##b=int(input('Enter the number b: '))
##def jog():
##    print(a+b)
##jog()
##print(a-b)
##output
##Enter the number a: 10
##Enter the number b: 20
##30
##-10

##global variable------------------------------------->global variable
##def sample(a):
##    print('inside1:',a)
##    global b
##    b=30
##    print('inside2:',b)
##a=10 ##global
##sample(a)
##print('outside:',b)
##output
##inside1: 10
##inside2: 30
##outside: 30

##global variable
##def sample(a):
##    print('inside1:',a)
##    global b
##    b=30
##    print('inside2:',b)
##a=10 
##sample(a)
##b=40
##print('outside:',b)
##output
##inside1: 10
##inside2: 30
##outside: 40

##global variable
##a=60
##b=80
##def sample(a):
##    print('inside1:',a)
##    global b
##    b=30
##    print('inside2:',b)
##a=10 
##sample(a)
##b=40
##print('outside:',b)
##output
##inside1: 10
##inside2: 30
##outside: 40

##sum of natural numbers
##a=int(input('Enter the number: '))
##i=1
##sum=0
##while i<=a:
##    sum=sum+i  
##    i=i+1
##print('THe sum is: ',sum)
##output
##Enter the number: 5
##THe sum is:  15

##sum of natural numbers
##a=int(input('Enter the number: '))
##i=1
##sum=0
##while i<=a:
##    sum=sum+i
##    print(sum)
##    i=i+1
##output
##Enter the number: 10
##1
##3
##6
##10
##15
##21
##28
##36
##45
##55

##sum of natural numbers
##n=int(input('Enter the number: '))
##s=0
##for i in range(1,n+1):
##    s=s+i
##print('The sum is: ',s)
##output:
##Enter the number: 5
##The sum is:  15

##recursion sum----------------------------------------------------->Recursion
##def add(n):
##    if n==1:
##        return 1
##    else:
##        return n+add(n-1) ##5+4+3+2+1
##print('The sum is:',add(n=int(input('Enter the number: '))))
##output:
##Enter the number: 10
##The sum is: 55

##recursion factorial----------------------------------------------------->Recursion
##def add(n):
##    if n==1:
##        return 1
##    else:
##        return n*add(n-1) ##5+4+3+2+1
##print('The factorial is:',add(n=int(input('Enter the number: '))))
##output:
##Enter the number: 5
##The factorial is: 120

##Fibnocci series
##n=int(input('Enter the number: '))
##a,b=0,1
##print(a,b,end=' ')
##for i in range(2,n):
##    c=a+b
##    print(c,end=' ')
##    a=b
##    b=c
##output:
##Enter the number: 10
##0 1 1 2 3 5 8 13 21 34 

##repeat function program 4 times
##def sam():
##    c=int(input('Enter the number: '))
##    if c==1:
##        print('excellent')
##    elif c==2:
##        print('very good')
##    elif c==3:
##        print('good')
##    else:
##        print('Invalid')
##sam()
##sam()
##sam()
##sam()

##def sam1():
##    a=10
##    b=20
##    c=a+b
##    print(c)
##def sam2():
##    a=10
##    b=20
##    c=a-b
##    print(c)
##sam1()
##sam2()





































































































