##prime number program using while loop
##n=int(input("Enter a number: "))
##count=0
##for i in range(1,n+1):
##    if n%i==0:
##        count=count+1
##if count==2:
##    print("It is Divisible",count,"times")
##    print("The number is a prime")
##else:
##    print("It is Divisible",count,"times")
##    print("The number is not prime")

##prime number program in a Range using while loop
##a,b=map(int,input().split())
##for n in range(a,b+1):
##   for i in range(2,(n//2)+1):
##      if n%i==0:
##        break
##   else:
##       print(n,end=' ')

##prime number program in a Range in reverse using while loop
##a,b=map(int,input().split())
##for n in range(a-1,b,-1):
##   for i in range(2,(n//2)+1):
##      if n%i==0:
##        break
##   else:
##       print(n,end=' ')

##prime number program in a Range in using while loop--------->both order and reverse
##a,b=map(int,input().split())
##if a<b:
##    s=1
##else:
##    s=-1
##for n in range(a,b+s,s):
##   for i in range(2,(n//2)+1):
##      if n%i==0:
##        break
##   else:
##       print(n,end=' ')
##calendar
##import calendar
##year=int(input("Enter the year: "))
##month=int(input("Enter the month: "))
##print(calendar.month(year,month))

##position of a prime number program using while loop
##n=int(input("Enter the number: "))
##c=0
##for i in range(1,n+1):
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        c=c+1
##print("The position of that number is:",c)

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

##students Random code picking one student in a Group----------->Random
##import random
##r=['22MH1A05F9','22MH1A05k2','22MH1A05i9','22MH1A05k4','22MH1A05k5','22MH1A05F3','22MH1A05G6','22MH1A05J7','22MH1A05L6',]
##n=random.choice(r)
##print(n)

            























            













