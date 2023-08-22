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






















