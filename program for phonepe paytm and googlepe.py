##program for phonepe ,paytm and googlepay
print('press 1 for phonepe')
print('press 2 for paytm')
print('press 3 for googlepay')
c=int(input('Enter your choice to send the money: '))
for i in range(1):
    if c==1:
          L=input('Enter the password for open the phonpe: ')
          if L=='1234':
              print('phonepe unlocked successfully')
          else:
              print('Wrong password')
              break
          amount=10000
          print('Your account balance: ',amount)
          c=int(input('Enter the amount to send the money: '))
          d=input('Enter Your UPI pin number: ')
          upipin='123456'
          if d==upipin:
              print(c,'Amount sended successfully')
              rem=10000-c
              print('Remaining balance in phonepe: ',rem)
              break
          else:
              print('Enter correct UPI pin')
    elif c==2:
          L=input('Enter the password for open the paytm: ')
          if L=='1234':
              print('paytm unlocked successfully')
          else:
              print('Wrong password')
              break
          amount=10000
          print('Your account balance: ',amount)    
          c=int(input('Enter the amount to send the money: '))
          d=input('Enter Your UPI pin number: ')
          upipin='123456'
          if d==upipin:
              print(c,'Amount sended successfully')
              amount=10000
              rem=10000-c
              print('Remaining balance in paytm: ',rem)
              break
          else:
              print('Enter correct UPI pin')
    elif c==3:
          L=input('Enter the password for open the googlepay: ')
          if L=='1234':
              print('googlepay unlocked successfully')
          else:
              print('Wrong password')
              break
          amount=10000
          print('Your account balance: ',amount)    
          c=int(input('Enter the amount to send the money: '))
          d=input('Enter Your UPI pin number: ')
          upipin='123456'
          if d==upipin:
              print(c,'Amount sended successfully')
              amount=10000
              rem=10000-c
              print('Remaining balance in googlepe: ',rem)
              break
          else:
              print('Enter correct UPI pin')
    else:
        print('Invalid')
        break
else:
    print('You enter Too many times')
    print('Your account blocked for 24 hours')
    print('It is not initiated by you call 2121')
    print('press 1 for relogin to change the UPI pin number')
    print('press 2 for old upi pin number and Aadhar number correctly')
    r=int(input('Enter your choice: '))
    if r==1:
          n=input('Enter your Atm card number last 3 digits : 34** **** *')
          m='123'
          if n==m:
                 g=int(input('Enter the new UPI pin number: '))
                 h=int(input('confirm the UPI pin: '))
                 if g==h:
                     print('Your UPI pin changed successfully')
                 else:
                     print('pin not matched')   
          else:
              print('Your UPI pin not changed successfully try after some time')
    elif r==2:
         y=input('Enter your Adhar number last 4 digits 1234 **** ')
         z=input('Enter your old UPI pin number: ')
         q='1234'
         k='123456'
         if y==q and z==k:
                 g=int(input('Enter the new UPI pin number: '))
                 h=int(input('confirm the UPI pin: '))
                 if g==h:
                     print('Your UPI pin changed successfully')
                 else:
                     print('pin not matched')
         else:
             print('Your UPI pin not changed successfully try after some time')

