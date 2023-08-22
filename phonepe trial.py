##program for phonepe ,paytm and googlepay
print('press 1 for phonepe')
print('press 2 for paytm')
print('press 3 for googlepay')
c=int(input('Enter your choice to send the money: '))
for i in range(1):
    if c==1:
          print('Thank you for choosing phonepe')
          print('creating an account on phonepe and to send the money')
          print('Some instructions you have to follow to create an account on phonepe')
          print('Fill the details correctly in the below')
          L=input('set the password for phonepe security purpose: ')
          lc=input('confirm the password: ')
          if L==lc:
              print('password created successfully')
          else:
              print('Wrong password')
              break
          h=input('Enter the password for opening phonepe: ')
          if h==lc:
              print('phonepe unclocked successfully')
          else:
              print('Wrong password')
              break
          ne=input('Enter your full name: ')
          um=int(input('Enter your mobile number linked with your bank account: '))
          en=input('Enter the bank name: ')
          ca=int(input('Enter the bank account number: '))
          at=int(input('Enter the ATM card number last last 6 digits 34** **** **'))
          va,li=map(int,input('ATM card valid upto for example 22/10: ').split('/'))
          print('For creating UPI ID')
          te=input('Enter your name: ')
          da=int(input('Enter your date of birth: '))
          print('The avaliable UPI ID with your name and date of birth are')
          print(te,da,'@axl')
          print(te,da,'@ybl')
          print(te,da,'@abl')
          print('press 1 for @axl')
          print('press 2 for @ybl')
          print('press 3 for @abl')
          cd=int(input('select one UPI ID: '))
          if cd==1:
             print('Your selected UPI Id is: ',te,da,'@axl')
             print('UPI ID created successfully')
          elif cd==2:
             print('Your selected UPI Id is: ',te,da,'@ybl')
             print('UPI ID created successfully')
          elif cd==3:
             print('Your selected UPI is: ',te,da,'@abl')
             print('UPI ID created successfully')
          else:
              print('Invalid UPI Id not matched')
              break
          up=input('create six digits UPI pin number: ')
          pi=input('confirm the UPI PIN number: ')
          if up==pi:
              print('UPI pin number generated successfully')
              print('Your phonepe account created successfully')
          else:
              print('Invalid UPI pin check and try again')
              break
          print('press 1 for continue the phonepe app to send the money')
          print('press 2 for closing the phonepe app')
          me=int(input('Enter your opinion: '))
          if me==1:
              print('opening phonepe')
          elif me==2:
              print('phonepe app closed')
              break
          else:
              print('Invalid option')
              break
          amount=10000
          print('Your bank account balance: ',amount)
          print('press 1 for senders mobile number')
          print('press 2 for senders UPI ID')
          e=int(input('Enter your option to send the payment method: '))
          if e==1:
              a=int(input('Enter the senders phonepe number: '))
          elif e==2:
              b=input('Enter the senders UPI ID: ')
          else:
              print('Invalid')
              break
          b=int(input('Enter the amount to send the money: '))
          d=input('Enter Your UPI pin number: ')
          if d==pi:
              print(b,'Rupees Amount sended successfully to this number: ',a)
              rem=10000-b
              print('Remaining balance in phonepe: ',rem)
              break
          else:
              print('Wrong UPI pin')
    elif c==2:
        print('Thank you for choosing paytm')
        print('creating an account on paytm and to send the money')
        print('Some instructions you have to follow to create an account on paytm')
        print('Fill the details correctly in the below')
        L=input('set the password for paytm security purpose: ')
        lc=input('confirm the password: ')
        if L==lc:
            print('password created successfully')
        else:
            print('Wrong password')
            break
        h=input('Enter the password for opening paytm: ')
        if h==lc:
            print('paytm unclocked successfully')
        else:
            print('Wrong password')
            break
        ne=input('Enter your full name: ')
        um=int(input('Enter your mobile number linked with your bank account: '))
        en=input('Enter the bank name: ')
        ca=int(input('Enter the bank account number: '))
        at=int(input('Enter the ATM card number last last 6 digits 34** **** **'))
        va,li=map(int,input('ATM card valid upto for example 22/10: ').split('/'))
        print('For creating UPI ID')
        te=input('Enter your name: ')
        da=int(input('Enter your date of birth: '))
        print('The avaliable UPI ID with your name and date of birth are')
        print(te,da,'@axl')
        print(te,da,'@ybl')
        print(te,da,'@abl')
        print('press 1 for @axl')
        print('press 2 for @ybl')
        print('press 3 for @abl')
        cd=int(input('select one UPI ID: '))
        if cd==1:
            print('Your selected UPI Id is: ',te,da,'@axl')
            print('UPI ID created successfully')
        elif cd==2:
            print('Your selected UPI Id is: ',te,da,'@ybl')
            print('UPI ID created successfully')
        elif cd==3:
            print('Your selected UPI is: ',te,da,'@abl')
            print('UPI ID created successfully')
        else:
            print('Invalid UPI Id not matched')
            break
        up=input('create six digits UPI pin number: ')
        pi=input('confirm the UPI PIN number: ')
        if up==pi:
            print('UPI pin number generated successfully')
            print('Your paytm account created successfully')
        else:
            print('Invalid UPI pin check and try again')
            break
        print('press 1 for continue paytm to send the money')
        print('press 2 for closing the paytm app')
        me=int(input('Enter your opinion: '))
        if me==1:
            print('paytm opened')
        elif me==2:
            print('phonepe app closed')
            break
        else:
            print('Invalid option')
            break
        amount=10000
        print('Your bank account balance: ',amount)
        print('press 1 for senders mobile number')
        print('press 2 for senders UPI ID')
        e=int(input('Enter your option to send the payment method: '))
        if e==1:
            a=int(input('Enter the senders paytm number: '))
        elif e==2:
            b=input('Enter the senders UPI ID: ')
        else:
            print('Invalid')
            break
        b=int(input('Enter the amount to send the money: '))
        d=input('Enter Your UPI pin number: ')
        if d==pi:
            print(b,'Rupees Amount sended successfully to this number: ',a)
            rem=10000-b
            print('Remaining balance in paytm: ',rem)
            break
        else:
            print('Wrong UPI pin')
          
    elif c==3:
        print('Thank you for choosing googlepay')
        print('creating an account on googlepay and to send the money')
        print('Some instructions you have to follow to create an account on googlepay')
        print('Fill the details correctly in the below')
        L=input('set the password for googlepay security purpose: ')
        lc=input('confirm the password: ')
        if L==lc:
            print('password created successfully')
        else:
            print('Wrong password')
            break
        h=input('Enter the password for opening googlepay: ')
        if h==lc:
            print('phonepe unclocked successfully')
        else:
            print('Wrong password')
            break
        ne=input('Enter your full name: ')
        um=int(input('Enter your mobile number linked with your bank account: '))
        en=input('Enter the bank name: ')
        ca=int(input('Enter the bank account number: '))
        at=int(input('Enter the ATM card number last last 6 digits 34** **** **'))
        va,li=map(int,input('ATM card valid upto for example 22/10: ').split('/'))
        print('For creating UPI ID')
        te=input('Enter your name: ')
        da=int(input('Enter your date of birth: '))
        print('The avaliable UPI ID with your name and date of birth are')
        print(te,da,'@axl')
        print(te,da,'@ybl')
        print(te,da,'@abl')
        print('press 1 for @axl')
        print('press 2 for @ybl')
        print('press 3 for @abl')
        cd=int(input('select one UPI ID: '))
        if cd==1:
            print('Your selected UPI Id is: ',te,da,'@axl')
            print('UPI ID created successfully')
        elif cd==2:
            print('Your selected UPI Id is: ',te,da,'@ybl')
            print('UPI ID created successfully')
        elif cd==3:
            print('Your selected UPI is: ',te,da,'@abl')
            print('UPI ID created successfully')
        else:
            print('Invalid UPI Id not matched')
            break
        up=input('create six digits UPI pin number: ')
        pi=input('confirm the UPI PIN number: ')
        if up==pi:
            print('UPI pin number generated successfully')
            print('Your googlepe account created successfully')
        else:
            print('Invalid UPI pin check and try again')
            break
        print('press 1 for continue the googlepay app to send the money')
        print('press 2 for closing the googlepay app')
        me=int(input('Enter your opinion: '))
        if me==1:
            print('opening googlepay')
        elif me==2:
            print('googlepay app closed')
            break
        else:
            print('Invalid option')
            break
        amount=10000
        print('Your bank account balance: ',amount)
        print('press 1 for senders mobile number')
        print('press 2 for senders UPI ID')
        e=int(input('Enter your option to send the payment method: '))
        if e==1:
            a=int(input('Enter the senders googlepay number: '))
        elif e==2:
            b=input('Enter the senders UPI ID: ')
        else:
            print('Invalid')
            break
        b=int(input('Enter the amount to send the money: '))
        d=input('Enter Your UPI pin number: ')
        if d==pi:
            print(b,'Rupees Amount sended successfully to this number: ',a)
            rem=10000-b
            print('Remaining balance in googlepay: ',rem)
            break
        else:
            print('Wrong UPI pin')
          
    else:
        print('Invalid option')
        break
else:
    print('You entered wrong password Too many times')
    print('Your account blocked for 24 hours for security purpose')
    print('It is not initiated by you call 23215')
    print('For relogin to your account select one option and give the credentials correctly')
    print('press 1 for ATM card number and ATM card validity date')
    print('press 2 for old UPI pin number and Aadhar number')
    r=int(input('Enter your choice: '))
    if r==1:
          n=input('Enter your Atm card number last 6 digits : 34** **** **')
          va,li=map(int,input('ATM card valid upto for example 22/10: ').split('/'))
          ca='AvDs'
          pt=input('Enter the captcha AvDs as it is: ')
          if ca==pt:
                 g=int(input('Enter the new UPI pin number: '))
                 h=int(input('confirm the UPI pin: '))
                 if g==h:
                     print('Your UPI pin changed successfully')
                 else:
                     print('pin not matched')   
          else:
              print('Your UPI pin not changed successfully try after some time')
    elif r==2:
         y=input('Enter your Adhar number last 4 digits 7869 **** ')
         z=input('Enter your old UPI pin number: ')
         mr='AvDs'
         zr=input('Enter the captcha A1D4 as it is: ')
         if mr==zr:
                 g=int(input('Enter the new UPI pin number: '))
                 h=int(input('confirm the UPI pin: '))
                 if g==h:
                     print('Your UPI pin changed successfully')
                 else:
                     print('pin not matched')
         else:
             print('Your UPI pin not changed successfully try after some time')
    else:
        print('Invalid option')

