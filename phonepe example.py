while i<=3:
                h=input('Enter the password for opening phonepe: ')
                if h==lc:
                    print('phonepe unclocked successfully')
                    break
                elif h!=lc:
                    print('Wrong password try again')
                else:
                    i==3
                    print('Your phone locked 30 seconds for security purpose')
                    break
