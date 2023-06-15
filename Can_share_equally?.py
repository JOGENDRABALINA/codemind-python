a,b=map(int,input().split())
a+b//2
if a%2==0 and a!=0:
    print('YES')
    
elif a==0 and b%2==0:
    print('YES')
else:
    print('NO')   