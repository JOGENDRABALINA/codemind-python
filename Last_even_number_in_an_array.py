n=int(input())
a=list(map(int,input().split()))
for i in range(-1,n-(2*n)-1,-1):
    if a[i]%2==0:
        print(a[i])
        break