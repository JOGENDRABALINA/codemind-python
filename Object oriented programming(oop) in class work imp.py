
##Basic program for classs
##class car():
##    pass
##a=car()
##print(a)

##b=car()
##print(b)
##output:
##<__main__.car object at 0x0000022884397010>
##<__main__.car object at 0x00000228866031D0>

##class jog():
##    pass
##a=jog()
##b=jog()
##print(a)
##print(b)

##constructor program
##class car:
##    def __init__(self):  #constructor
##        print('Jogendra')
##a=car()
##print(a)
##output:
##Jogendra
##<__main__.car object at 0x000002B6404DAED0>

##constructor program
##class car:
##    def __init__(self,name,modal):  #constructor
##        print('Jogendra Your car names with modals')
##        self.name=name
##        self.modal=modal
##    def display(self):
##        print(self.name,self.modal)
##a=car('Range Rover',1234)
##a.display()
##
##b= car('Benz',5678)
##b.display()

##output:
##Jogendra Your car names with modals
##Range Rover 1234
##Jogendra Your car names with modals
##Benz 5678

##constructor program
##class bike:
##    def __init__(self,name,modal):  #constructor
##        print('Jogendra Your bike names with modals')
##        self.name=name
##        self.modal=modal
##    def display(self):
##        print(self.name,self.modal)
##a=bike('DUKE',360)
##a.display()
##
##b=bike('KTM',400)
##b.display()

##output:
##Jogendra Your bike names with modals
##DUKE 360
##Jogendra Your bike names with modals
##KTM 400

##constructor program
##class student:
##    def __init__(self,name,Rollno,st1,st2):  #constructor
##        print('')
##        self.name=name
##        self.Rollno=Rollno
##        self.st1=st1
##        self.st2=st2
##    def display(self):
##        print(self.name,self.Rollno,(self.st1+self.st2)//2)
##a=student('Jogendra','22MH1A05F9',80,90)
##a.display()
##
##b=student('Srinivas','22MH1A05F9',60,70)
##b.display()

##output:
##Jogendra 22MH1A05F9 85
##
##Srinivas 22MH1A05F9 65

##constructor program
##class student:
##    def __init__(self,name,roll,s1,s2):  #constructor
##        self.name=name
##        self.roll=roll
##        self.s1=s1
##        self.s2=s2
##    def display(self):
##        print('Name: ',self.name)
##        print('Roll no: ',self.roll)
##        print('Average marks: ',(self.s1+self.s2)/2)
##print('class 1st')
##a=student('Jogendra','22MH1A05F9',95,90)
##a.display()
##print('class 2nd')
##b=student('Srinivasu','22MH1A05K2',80,85)
##b.display()

##output:
##class 1st
##Name:  Jogendra
##Roll no:  22MH1A05F9
##Average marks:  92.5
##class 2nd
##Name:  Srinivasu
##Roll no:  22MH1A05K2
##Average marks:  82.5

##class student:
##    college='Aditya'  #class static
##    def __init__(self,name,roll,s1,s2):  #constructor
##        self.name=name
##        self.roll=roll
##        self.s1=s1
##        self.s2=s2
##        print('Details')
##    def display(self):
##        print('Name: ',self.name)
##        print('Roll no: ',self.roll)
##        print('Average marks: ',(self.s1+self.s2)/2)
##        print(self.college)
##print('class 1st')
##a=student('Jogendra','22MH1A05F9',95,90)
##a.display()
##print('class 2nd')
##b=student('Srinivasu','22MH1A05K2',80,85)
##b.display()

##output:
##class 1st
##Details
##Name:  Jogendra
##Roll no:  22MH1A05F9
##Average marks:  92.5
##Aditya
##class 2nd
##Details
##Name:  Srinivasu
##Roll no:  22MH1A05K2
##Average marks:  82.5
##Aditya

##class student:
##    college='Aditya'  #class static
##    def __init__(self,name,roll,s1,s2,college):  #constructor
##        self.name=name
##        self.roll=roll
##        self.s1=s1
##        self.s2=s2
##        self.college=college
##        print('Details')
##    def display(self):
##        print('Name: ',self.name)
##        print('Roll no: ',self.roll)
##        print('Average marks: ',(self.s1+self.s2)/2)
##        print(self.college)
##print('class 1st')
##a=student('Jogendra','22MH1A05F9',95,90,'ACOE')
##a.display()
##print('class 2nd')
##b=student('Srinivasu','22MH1A05K2',80,85,'ACOE')
##b.display()
####output:
##class 1st
##Details
##Name:  Jogendra
##Roll no:  22MH1A05F9
##Average marks:  92.5
##ACOE
##class 2nd
##Details
##Name:  Srinivasu
##Roll no:  22MH1A05K2
##Average marks:  82.5
##ACOE

##*******
##class student:
##    college='Aditya'  #class static
##    def __init__(self,name,roll,s1,s2,college):  #constructor
##        self.name=name
##        self.roll=roll
##        self.s1=s1
##        self.s2=s2
##        self.college=college
##    def display(self):
##        print(self.name,self.roll,(self.s1+self.s2)/2,self.college)
##    @classmethod
##    def classm(cls):
##        cls.college='ACOE'
##        print(cls.college)
##a=student('Jogendra','22MH1A05F9',95,90,'ACOE')
##a.display()
##a.classm()
####output:
##Jogendra 22MH1A05F9 92.5 ACOE
##ACOE

##*******
##class student:
##    college='Aditya'  #class static
##    def __init__(self,name,roll,s1,s2,college):  #constructor
##        self.name=name
##        self.roll=roll
##        self.s1=s1
##        self.s2=s2
##        self.college=college
##    def display(self):
##        print(self.name,self.roll,(self.s1+self.s2)/2,self.college)
##    @classmethod
##    def classm(cls):
##        cls.college='ACOE'
##        print(cls.college)
##    @staticmethod
##    def sample():
##        print('Hello')
##a=student('Jogendra','22MH1A05F9',95,90,'ACOE')
##a.sample()
####output:
##Hello







































