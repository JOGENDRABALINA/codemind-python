n=int(input("Enter the number: "))
rev=n
r=0
while n>0:
    rem=n%10
    r=r*10+rem
    n//=10
if rev==r:
    print("The number is a Palindrome")
else:
    print("The number is Not palindrome")
