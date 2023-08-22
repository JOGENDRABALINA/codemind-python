##-------------------------------------------------------------------------->INHERITANCE

##class person():
##    def __init__(self,name,aadhar):
##        self.name=name
##        self.aadhar=aadhar
##    def display(self):
##        print(self.name,self.aadhar)
##
##class student(person):
##    def __init__(self,name,aadhar,roll,branch):
##        self.roll=roll
##        self.branch=branch
##        super().__init__(name,aadhar)
##    def display(self):
##        print(self.name,self.aadhar,self.roll,self.branch)
##s=student('Jogendra','5242 8765 2344','22MH1A05F9','CSE')
##s.display()
##output:
##Jogendra 5242 8765 2344 22MH1A05F9 CSE

##def sample():
##    a=10
##    b=20
##    print(a+b);print(a-b);print(a*b);print(a/b)
##sample()
##output:
##30
##-10
##200
##0.5

##class person():
##    college='ADITYA'          #----------------------------------------------------------------->4th preferance
##    def __init__(self,name,aadhar,college):
##        self.name=name
##        self.aadhar=aadhar
##        self.college=college  #----------------------------------------------------------------->2nd preferance
##    def display(self):
##        print(self.name,self.aadhar)
##
##class student(person):
##    college='ACOE'    #----------------------------------------------------------------->3rd preferance
##    def __init__(self,name,aadhar,roll,branch,college):
##        self.roll=roll
##        self.branch=branch
##        self.college=college
##        super().__init__(name,aadhar,college)
##    def display(self):
##        print(self.name,self.aadhar,self.roll,self.branch,self.college)
##s=student('Jogendra','5242 8765 2344','22MH1A05F9','CSE','acoe')       #----------------------------------------------------------------->1st preferance
##s.display()
##output:
##Jogendra 5242 8765 2344 22MH1A05F9 CSE acoe

##class person():
##    college='ADITYA'
##    def __init__(self,name,aadhar,college):
##        self.name=name
##        self.aadhar=aadhar
##        #self.college=college
##    def display(self):
##        print(self.name,self.aadhar)
##
##class student(person):
##    #college='ACOE'
##    def __init__(self,name,aadhar,roll,branch,college):
##        self.roll=roll
##        self.branch=branch
##        #self.college=college
##        super().__init__(name,aadhar,college)
##    def display(self):
##        print(self.name,self.aadhar,self.roll,self.branch,self.college)
##s=student('Jogendra','5242 8765 2344','22MH1A05F9','CSE','acoe')
##s.display()
##output:
##Jogendra 5242 8765 2344 22MH1A05F9 CSE ADITYA

##over riding
##class coding():
##    def display(self):
##        print('Coding has some rules')
##class python(coding):
##    def display(self):
##        print('python has indentation')
##class java(coding):
##    def dispaly(self):
##        print('Java has braces')
##a=coding()
##a.display()
##b=python()
##b.display()

####over loading
##class example():
##    def sample(self):
##        print('Jogendra')
##    def sample(self,a):
##        print('Hello',a)
##a=example()
##a.sample('Python')

####over loading
##class example():
##    def sample(self):
##        print('Jogendra')
##class example1(example):
##    def sample(self,b):
##        print('Hello',b)
##b=example()
##b.sample()
##
##a=example1()
##a.sample('Python')

##over loading
class example():
    def display(self):
        print('Jogendra')
    def sample(self):
        print('Hello')
a=example()
a.display()
a.sample()
    





















