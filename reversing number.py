##1.reversing the number using while loop
n=int(input("Enter a number: "))
r=0
while n>0:
    rem=n%10
    print("Remainder:",rem)
    r=r*10+rem
    print("r:",r)
    n//=10
    print("Number:",n)
print("After reversing the number is: ",r)
