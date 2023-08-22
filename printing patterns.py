##pattern programs printing 1 to 5 5 times
##for i in range(1,6):
##    for j in range(1,6):
##        print(j,end=' ')
##    print()##--------------------->output printing in the next line
##
##pattern programs printing logic 5 times
##for i in range(1,6):
##    for j in range(1,6):
##        print(i+j,end=' ')
##    print()##--------------------->output printing in the next line
##
##pattern programs printing  5 times
##for i in range(1,6):
##    for j in range(1,6):
##        print(i*j,end=' ')
##    print()##--------------------->output printing in the next line
##
##
##pattern programs printing  pyramid right angle triangle
##n=int(input('Enter the number:'))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()##--------------------->output printing in the next line
##
##printing pattern
##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()
##    
##output
##5
##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5 
####printing zero
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n: 
##             print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output
##5
##* * * * * 
##*       * 
##*       * 
##*       * 
##* * * * *
##
##printing zero
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n: 
##             print(j,end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output
##1 2 3 4 5 
##1       5 
##1       5 
##1       5 
##1 2 3 4 5 
##
##printing plus
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==3  or j==3: 
##             print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output
##Enter the number: 5
##    *     
##    *     
##* * * * * 
##    *     
##    *     
##
##printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==3 or i==n  or j==3 or j==n or i==1 or j==1: 
##             print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output
##Enter the number: 5
##* * * * * 
##*   *   * 
##* * * * * 
##*   *   * 
##* * * * * 
##
##printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n  or j==1 or j==n or i==3 or j==3: 
##             print(i,end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output
##Enter the number: 5
##1 1 1 1 1 
##2   2   2 
##3 3 3 3 3 
##4   4   4 
##5 5 5 5 5 
##
##printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i%2==0 and j%2==0:
##             print('',end=' ')
##        else:
##            print('i',end=' ')
##    print()
##output
##Enter the number: 5
##1 1 1 1 1 
##2   2   2 
##3 3 3 3 3 
##4   4   4 
##5 5 5 5 5
##
##printing using ---------->while loop
##n=int(input('Enter the number: '))
##i=1
##while i<=n:
##    j=1
##    while j<=n:
##        if i==(n//2)+1 or i==1  or j==1 or j==(n//2)+1 or i==n or j==n:
##             print('*',end=' ')
##        else:
##            print(' ',end=' ')
##        j=j+1
##    print()
##    i=i+1
##output
##Enter the number: 5
##* * * * * 
##*   *   * 
##* * * * * 
##*   *   * 
##* * * * * 
##
##printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for k in range(1,n-i+1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##         print('*',end=' ')
##    print()           
##output
##Enter the number: 5
##        * 
##      * * 
##    * * * 
##  * * * * 
##* * * * * 

####printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if j==1 or j==n or i==3:  
##             print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##output:
##Enter the number: 5
##*       * 
##*       * 
##* * * * * 
##*       * 
##*       * 

##printing
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for k in range(1,n-i+1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##         print('*  ',end=' ')
##    print()           
##output
##Enter the number: 5
##        *   
##      *   *   
##    *   *   *   
##  *   *   *   *   
##*   *   *   *   *   

##printing
##n=int(input('Enter the number: '))
##for i in range(n,0,-1):
##    for k in range(1,n-i+1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##         print(' * ',end=' ')
##    print()           
##output
##Enter the number: 10
## *   *   *   *   *   *   *   *   *   *  
##   *   *   *   *   *   *   *   *   *  
##     *   *   *   *   *   *   *   *  
##       *   *   *   *   *   *   *  
##         *   *   *   *   *   *  
##           *   *   *   *   *  
##             *   *   *   *  
##               *   *   *  
##                 *   *  
##                   *  

##printing--------------->Easy Method
##n=int(input('Enter the number: '))
##for i in range(1,n+1):
##    for k in range(1,i+1):
##        print(' ',end=' ')
##    for j in range(1,n-i+1):
##         print(' * ',end=' ')
##    print()    
##output
##Enter the number: 5
##   *   *   *   *  
##     *   *   *  
##       *   *  
##         * 

##printing character ------------------------------>character
##n=int(input('Enter the character: '))
##for i in range(n):
##    for j in range(65,65+i+1):
##        print(chr(j),end=' ')
##    print()

##-------------------------------------------------->my own
