#Account blocked
Name='Jogendra'
password='12345'
for i in range(1,2):
    a=input('Enter your name: ')
    b=input('Enter your password: ')
    if a==Name:
        print('Login Succesfully')
    elif b==password:
        print('Login Successfully')
        break
    else:
        print('Invalid credentials')
else:
    print('Your Account blocked 24 hours for security purpose')
    print('It is not initiated by you call 2421')
    print('For reLogin')
    card='123'
    valid='22'
    c=int(input('Enter your ATM card number last three digits 34** *** '))
    d=int(input('You card valid upto: '))
    if card==c:
        print('Login Succesfully')
    elif valid==d:
        print('Login Succesfully')
        
##Account blocked
##did='jog@2003'
##dpw='12345'
##for i in range(5):
##    uid=input('Enter your name: ')
##    upw=input('Enter your password: ')
##    if did==uid and dpw==upw:
##        print('Login Succesfully')
##        break
##    else:
##        print('Invalid Credentials')
##else:
##    print('Your Account blocked for 24 hours')

##Account blocked
##pin='1234'
##upipin='123456'
##for i in range(3):
##    a=input('Enter your pin number: ')
##    b=input('Enter your upi pin number: ')
##    if pin==a and upipin==b:
##        c=input('Enter the amount: ')
##        c=='200'
##        print('Amount send successfully')
##        break
##    else:
##        print('Invalid Credentials')
##else:
##    print('Your Account blocked for 24 hours')
##    print('It is not initiated by you call 2121')


##phonepe and paytm-------------------------------------------------------------->phonepe and paytm
##print('press 1 for phonepe')
##print('press 2 for paytm')
##print('press 3 for googlepay')
##for i in range(1):
##    c=int(input('Enter your choice: '))
##    if c==1:
##          L=input('Enter the password for open the phonpe: ')
##          if L=='4321':
##              print('phonepe unlocked successfully')
##          else:
##              print('Enter the correct password')
##          c=input('Enter the amount: ')
##          d=input('Enter UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print('Amount send successfully')
##              break
##          else:
##              print('Enter correct UPI pin')
##    elif c==2:
##          L=input('Enter the password for open the paytm: ')
##          if L=='4321':
##              print('paytm unlocked successfully')
##          else:
##              print('Enter the correct password')
##          c=input('Enter the amount: ')
##          d=input('Enter UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print('Amount send successfully')
##              break
##          else:
##              print('Enter correct UPI pin')
##    elif c==3:
##          L=input('Enter the password for open the googlepay: ')
##          if L=='4321':
##              print('googlepay unlocked successfully')
##          else:
##              print('Enter the correct password')
##          c=input('Enter the amount: ')
##          d=input('Enter UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print('Amount send successfully')
##              break
##          else:
##              print('Enter correct UPI pin')
##else:
##    print('You enter Too many times')
##    print('Your account blocked for 24 hours')
##    print('It is not initiated by you call 2121')
##    print('press 1 for relogin to change the UPI pin number')
##    print('press 2 for old upi pin nimber correctly')
##    r=int(input('Enter your choice: '))
##    if r==1:
##          n=input('Enter your Atm card number last 3 digits : 34** **** *')
##          m='123'
##          if n==m:
##                 g=input('Enter the new UPI pin number: ')
##                 print('Your UPI pin changed successfully')
##          else:
##              print('Your UPI pin not changed successfully try after some time')
##    elif r==2:
##         y=input('Enter your Adhar number last 4 digits 1234 **** ')
##         z=input('Enter your old UPI pin number: ')
##         q='1234'
##         k='123456'
##         if y==q and z==k:
##             g=input('Enter the new UPI pin number: ')
##             print('Your UPI pin changed successfully')
##         else:
##             print('Your UPI pin not changed successfully try after some time')
##    
##         
              
##program for phonepe ,paytm and googlepay-------------------->original program
##print('press 1 for phonepe')
##print('press 2 for paytm')
##print('press 3 for googlepay')
##c=int(input('Enter your choice to send the money: '))
##for i in range(1):
##    if c==1:
##          L=input('Enter the password for open the phonpe: ')
##          if L=='1234':
##              print('phonepe unlocked successfully')
##          else:
##              print('Wrong password')
##              break
##          amount=10000
##          print('Your account balance: ',amount)
##          c=int(input('Enter the amount to send the money: '))
##          d=input('Enter Your UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print(c,'Amount sended successfully')
##              rem=10000-c
##              print('Remaining balance in phonepe: ',rem)
##              break
##          else:
##              print('Enter correct UPI pin')
##    elif c==2:
##          L=input('Enter the password for open the paytm: ')
##          if L=='1234':
##              print('paytm unlocked successfully')
##          else:
##              print('Enter the correct password')
##          amount=10000
##          print('Your account balance: ',amount)    
##          c=int(input('Enter the amount to send the money: '))
##          d=input('Enter Your UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print(c,'Amount sended successfully')
##              amount=10000
##              rem=10000-c
##              print('Remaining balance in paytm: ',rem)
##              break
##          else:
##              print('Enter correct UPI pin')
##    elif c==3:
##          L=input('Enter the password for open the googlepay: ')
##          if L=='1234':
##              print('googlepay unlocked successfully')
##          else:
##              print('Enter the correct password')
##          amount=10000
##          print('Your account balance: ',amount)    
##          c=int(input('Enter the amount to send the money: '))
##          d=input('Enter Your UPI pin number: ')
##          upipin='123456'
##          if d==upipin:
##              print(c,'Amount sended successfully')
##              amount=10000
##              rem=10000-c
##              print('Remaining balance in googlepe: ',rem)
##              break
##          else:
##              print('Enter correct UPI pin')
##    else:
##        print('Invalid')
##        break
##else:
##    print('You enter Too many times')
##    print('Your account blocked for 24 hours')
##    print('It is not initiated by you call 2121')
##    print('press 1 for relogin to change the UPI pin number')
##    print('press 2 for old upi pin number and Aadhar number correctly')
##    r=int(input('Enter your choice: '))
##    if r==1:
##          n=input('Enter your Atm card number last 3 digits : 34** **** *')
##          m='123'
##          if n==m:
##                 g=int(input('Enter the new UPI pin number: '))
##                 h=int(input('confirm the UPI pin: '))
##                 if g==h:
##                     print('Your UPI pin changed successfully')
##                 else:
##                     print('pin not matched')   
##          else:
##              print('Your UPI pin not changed successfully try after some time')
##    elif r==2:
##         y=input('Enter your Adhar number last 4 digits 1234 **** ')
##         z=input('Enter your old UPI pin number: ')
##         q='1234'
##         k='123456'
##         if y==q and z==k:
##                 g=int(input('Enter the new UPI pin number: '))
##                 h=int(input('confirm the UPI pin: '))
##                 if g==h:
##                     print('Your UPI pin changed successfully')
##                 else:
##                     print('pin not matched')
##         else:
##             print('Your UPI pin not changed successfully try after some time')

                 
          
    
      















