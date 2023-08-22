##Fibonacci program using for loop
##n=int(input("Enter the number: "))
##a=0
##b=1
##c=a+b
##print(a,b,end=' ')
##for i in range(2,n):
##        c=a+b
##        print(c,end=' ')
##        a=b
##        b=c

##Fibonacci program using while
n=int(input("Enter the number: "))
a=0
b=1
c=a+b

print(a,b,end=' ')
i=2
while i<n:
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        i=i+1
