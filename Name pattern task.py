##printing name
print('1 for H name')
print('2 for Jogendra')
c=int(input('Enter the number 1 or 2: '))
if c==1:
    n=int(input('Enter the number: '))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==3:  
                 print('H',end=' ')
            else:
                print(' ',end=' ')
        print()
    print('R R R R ')
    print('R       R')
    print('R       R')
    print('R R R R ')
    print('R R'  )
    print('R   R')
    print('R     R')
    print('R       R')
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==n or j==n:  
                 print('U',end=' ')
            else:
                print(' ',end=' ')
        print()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==3:
                print('T',end=' ')
            else:
                print(' ',end=' ')
        print()         
                                        
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==3:
                print('H',end=' ')
            else:
                print(' ',end=' ')
        print()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if  i==1 or i==n or j==3:
                print('I',end=' ')
            else:
                 print(' ',end=' ')
        print()
    print('K      K')
    print('K     K')
    print('K   K')
    print('K K')
    print('K  K')
    print('K   K')
    print('K    K')

    print('       A')
    print('     A   A')
    print('    A     A')
    print('   A  A A  A')
    print('  A         A')
    print(' A           A')
    print('A             A')
  
elif c==2:
    n=int(input('Enter the number: '))
    print('J  J  J  J  J')
    print('      J    ')
    print('      J    ')
    print('      J    ')
    print('      J    ')
    print('      J   ')
    print('J J J     ')
    for i in range(1,n+1):
        for j in range(1,n+1):
            if  i==1 or i==n or j==1 or j==n:
                print('o',end=' ')
            else:
                print(' ',end=' ')
        print()
    print('  G G G G')
    print('G ')
    print('G      ')
    print('G   G G G G ')
    print('G      G  G')
    print(' G  G G   G ')
    print('          G')
    print('          G')
    for i in range(1,n+1):
        for j in range(1,n+1):
            if  i==1 or i==n or j==1 or i==3:
                print('E',end=' ')
            else:
                print(' ',end=' ')
        print()
    print('N N       N')
    print('N  N      N')
    print('N   N     N')
    print('N    N    N')
    print('N     N   N')
    print('N      N  N')
    print('N       N N')

    print('D D D D')
    print('D       D')
    print('D       D')
    print('D       D')
    print('D       D')
    print('D       D')
    print('D D D D')

    print('R R R R ')
    print('R       R')
    print('R       R')
    print('R R R R ')
    print('R R'  )
    print('R   R')
    print('R     R')
    print('R       R')

    print('       A')
    print('     A   A')
    print('    A     A')
    print('   A  A A  A')
    print('  A         A')
    print(' A           A')
    print('A             A')
else:
    print('Manishi venaa nuvvu asalu 1 0r 2 enter cheyyamante')
    print('Chi pora')


