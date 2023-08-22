##c=str(input('ENter password: '))
##lock='abc'
##if lock==c:
##    print('correct')
##else:
##    print('chi poora')

##b=30
##def sam():
##    a=10
##    b=10
##    c=a+b
##    print(c)
##    print('Jogendra')
##sam()
##print(b)
##sam()


##def sample(n):#formal parameters
##    if n%2==0:
##        print(n,'is Even number')
##    else:
##        print(n,'is Odd number')
##a=int(input('Enter the number: '))#actual parameters
##sample(a)













##weight=int(input())
##pounds=weight*2.2
##print(pounds)

##a=int(input())
##b=int(input())
##c=int(input())
##sum=a+b+c
##average=(a+b+c)/3
##print(sum)
##print(average)

##for i in range(8,90,3):
##    print(i,end="  ")


##name=input()
##n=int(input())
##print(name*n)

##for i in range(1,5):
##    for j in range(i):
##        print('*',end=" ")
##    print()


##import random
##r=random.randint(1,10)
##while True:
##    guess=int(input())
##    if r==guess:
##        print('congrants')
##        break
##    else:
##        print('not')

##n=int(input("Enter how many times your name print:  "))
##for i in range(1,n):
##    print('HARI KEERTHANA',end='  ')

##n=input("Enter your name: ")
##print('press 1 for keerthana')
##print('press 2 for jogendra')
##c=int(input('Enter your choice: '))
##if c==1:
##    print('Idiot')
##elif c==2:
##    print('stupid')
##else:
##    print('Chi poora')

##n=int(input())
##for i in range(1,n):
##    for j in range(1,n):
##        print(i,'x',j,'=',i*j)
##    print()
    
##a=1911
##for i in range(1,5):
##    n=int(input("Enter your password: "))
##    if a==n:
##        print('phone unlocked successfully')
##        print('Hii harikeerthana')
##        print('Iam your mobile phone')
##        break
##    else:
##        print('Wrong password! Try again')
##else:
##    print('Your account blocked for 24 hours')
    
##import random
##c=random.randint(1,10)
##while True:
##    g=int(input('Enter one number: '))
##    if c==g:
##        print('you are correct')
##        break
##    else:
##        print('Your Wrong ! Try again')


##print('How many states in India?')
##c=29
##print('a.27            b.28               c.29            d.56')
##d=int(input('Ans: '))
##if c==d:
##      print('correct')
##else:
##    print('Wrong')

##n=int(input('Enter how many times your name print: '))
##for i in range(1,n):
##    print('Rama',end='        ' )

##n=int(input('Enter the number: '))
##for i in range(1,n):
##    for j in range(1,n):
##        print(i,'x',j,'=',i*j)
##
##    print()






##total={}
##def insert(items):
##    if items in total:
##        total[items]+=1
##    else:
##        total[items]=1
##insert('Apple')
##insert('Ball')
##insert('Apple')
##print(len(total))


##a=[1,2,3,4,4,8,7,8,7]
##a.reverse()
##print(a)


##def a234():
##    a=10
##    b=20
##    print(a+b)
##a234()

##for i in range(1,150000):
##    print(chr(i),end='   ')

##def my_function(): 
##
##                x = 10 
##
##                y = 20 
##
##                print("Local variables:", locals()) 
##
##                print("Global variables:", globals())
##my_function() 
##
##def check_pass_fail(mark): 
##
##    if mark >= 40: 
##
##        return "Pass" 
##
##    else: 
##
##        return "Fail" 
##
### Read the subject mark from the user 
##
##mark = int(input("Enter the subject mark: ")) 
##
### Call the function and print the result 
##
##result = check_pass_fail(mark) 

##print(result) 

##class Employee: 
##
##    def __init__(self, name, department, salary): 
##
##        self.name = name 
##
##        self.department = department 
##
##        self.salary = salary 
##
##  
##
##    def read_employee_info(self): 
##
##        self.name = input("Enter employee name: ") 
##
##        self.department = input("Enter employee department: ") 
##
##        self.salary = float(input("Enter employee salary: ")) 
##
##  
##
##    def print_employee_info(self): 
##
##        print("Employee Name:", self.name) 
##
##        print("Department:", self.department) 
##
##        print("Salary:", self.salary)
##
##emp = Employee("John Doe", "IT", 5000)
##
### Print employee info
##emp.print_employee_info()
##
### Update employee info by reading from user input
##emp.read_employee_info()
##
### Print updated employee info
##emp.print_employee_info()

##try:  
##
##       numerator = int(input("Enter the numerator: ")) 
##
##       denominator = int(input("Enter the denominator: ")) 
##
##       result = numerator / denominator  
##
##except ZeroDivisionError:  
##
##       print("Error: Division by zero is not allowed.")  
##
##else: 
##
##       print("The result of division is:", result)  
##
##finally:  
##
##       print("Thank you for using the program!") 

##try:  
##
##      # Example 1: Division by zero  
##
##      result = 10 / 0  
##
##      # Example 2: Accessing an undefined variable  
##
##      print(undefined_variable)  
##
##      # Example 3: Index out of range  
##
##      my_list = [1, 2, 3]  
##
##      print(my_list[5])  
##
##except ZeroDivisionError:  
##
##      print("Error: Division by zero")  
##
##except NameError:  
##
##      print("Error: Variable is not defined")  
##
##except IndexError:  
##
##      print("Error: Index is out of range")  
##
##finally:  
##
##      print("Program execution completed.") 

##n=int(input())
##r=1
##for i in range(1,n+1):
##      if n%i==0:
##            r=r*i
##            print(r)
##

##def add():
##    a=list(map(int,input().split()))
##    b=sum(a)
##    print(b)
##add()

##a="Helloworld"
##s="e"+"H"+a[2:8]+"d"+"l"
##print("The reverse order of last and first two characters: ",s)

n=int(input())
i=1
s=0.0
while i<n+1:
    s=s+1.0/i
    print(s)
    i=i+1
    

    












          


