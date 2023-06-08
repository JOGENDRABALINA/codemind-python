'''There will be a name error in this program and the execution stops at error '''
##try and except
##try:
##    a=10
##    print(a+b)
##except:
##    print('Jogendra')
##output:
##Jogendra

'''if there is no error in the try block the error block will be printed and except block is skipped even it is right'''
##try and except
##try:
##    a=10
##    b=20
##    print(a+b)
##except:
##    a=20
##    b=30
##    print(a+b)
##output:
##30

##try and except
##try:
##    a=10
##    b=20
##    print(a+b)
##    print(a+'k')
##except NameError:
##    print('Jogendra')
##except TypeError:
##    print('Hello')
##output:
##30
##Hello

##try and except
##try:
##    a=10
##    b=20
##    print(a+b)
##except NameError:
##    print('Jogendra')
##except TypeError:
##    print('Hello')
##output:
##30

##try and except
##try:
##    a=10
##    print(a)
##except:
##    print('Jogendra')
##else:
##    print('Hello')
##output:
##10
##Hello

##try and except
##try:
##    a=10
##    print(a)
##except:
##    print('Jogendra')
##else:
##    print('Hello')
##finally:
##    print('DOne')
##output:
##10
##Hello
##DOne

##try and except
##try:
##    a=10
##    print(b)
##except:
##    a=10
##    b=20
##    print(a+b)
##else:
##    print('Jogendra')
##finally:
##    print('Done')
##output:
##30
##Done

##try and except
a=int(input('Enter your marks: '))
try:
    if a>=0 and a<=100:
        if a>40:
            print('Pass')
        
        else:
            print('Fail')
    else:
        raise NameError
except NameError:
    print('please enter valid marks')
##output:
##Enter your marks: 1000
##please enter valid marks
    























































































