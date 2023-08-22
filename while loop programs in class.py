##------------->while loop
##i=1
##while i<=10:
##    print(i)
##    i=i+1

##Name printing 10 times
##i=1
##while i<=10:
##    print("JOGENDRA")
##    i=i+1

##sum of numbers
##i=1
##sum=0
##while i<=10:
##    sum=sum+i
##    print(sum)
##    i=i+1

##table printing
##n=int(input("Enter a number: "))
##i=1
##while i<=10:
##    print(n,'x',i,'=',n*i)
##    i=i+1

##printing -10 numbers to +10
##i=-10
##while i<10:
##     i=i+1
##     if i==0:
##        continue##---------------skipping zero
##     print(i)  
    
##printing 1 to 10 skipping 0
##i=-10
##while i<10:
##     i=i+1
##     if i<0:
##        continue##---------------skipping zero
##     print(i) 

##printing divisible of 5---------------->using continue
##i=1
##while i<30:
##    i=i+1
##    if i%5!=0:
##        continue
##    print(i,end=' ')
    
##printing divisible of 5
##i=5
##while i<=30:
##    print(i,end=' ')
##    i=i+5

##printing divisible of 5
##i=1
##while i<=30:
##    print(i*5,end=' ')
##    i=i+1

##printing divisible of 5 in reverse without using continue
##i=6
##while i>0:
##    print(i*5,end=' ')
##    i=i-1
    
##printing divisible of 5 in reverse using continue
##i=31
##while i>1:
##    i=i-1
##    if i%5!=0:
##        continue
##    print(i,end=' ')
    

##----------------------------------------------else also uses in for loop and while loop
####program for wrong credentials 5 times locked
##did='jogendra@2003'
##dpw='12345'
##for i in range(5):
##    uid=input("Enter your Emil-id: ")
##    upw=input("Enter your password: ")
##    if did==uid and dpw==upw:
##        print('Login successfully')
##        break
##    else:
##        print('Wrong credentials')
##else:
##    print('Account blocked for 24 hours')
        
##program for wrong credentials 5 times locked without using else
##did='jogendra@2003'
##dpw='12345'
##s=0
##for i in range(5):
##    uid=input("Enter your Emil-id: ")
##    upw=input("Enter your password: ")
##    if did==uid and dpw==upw:
##        print('Login successfully')
##        break
##    else:
##        print('Wrong credentials')
##        s=s+1
##if s==5:
##    print('Account blocked for 24 hours')

##while loop programs-------------------->while loop
##1.reversing the number----------------------------------------->Reversing
##n=int(input("Enter a number: "))
##r=0
##while n>0:
##    rem=n%10
##    print("Remainder:",rem)
##    r=r*10+rem
##    print("r:",r)
##    n//=10
##    print("Number:",n)
##print("After reversing the number is: ",r)

##2.reversing the number correct method
##n=int(input("Enter a number: "))
##print("After reversing the number is: ",str(n)[::-1])

##prime number or not-------------------------------------------------------------------->prime
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


####prime number or not second model
##n=int(input("Enter a number: "))
##for i in range(2,n):
##    if n%i==0:
##        print("It is Divisible",i,"times")
##        print("Is it prime?:",False)
##        break
##else:
##    print("Is it prime?:",True)

##prime number or not Third model
##n=int(input("Enter a number: "))
##for i in range(2,(n//2)+1):
##    if n%i==0:
##        print("It is Divisible",i,"times")
##        print("Is it prime?:",False)
##        break
##else:
##    print("Is it prime?:",True)


















