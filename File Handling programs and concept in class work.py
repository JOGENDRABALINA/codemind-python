'''X -> create a file
W -> create and write
a -> create and write
r -> Read'''

##creating a file and opening
##with open(r'Hii.txt','r') as f:
##    a=f.read()
##    print(a)
##output:
##Hii Jogendra
##How are you
##Are you studying well

##creating a file and opening
##d=open(r'Hii.txt','r')
##s=d.readlines()
##for i in s:
##    print(i)
##d.close()
##output:
##Hii Jogendra
##
##How are you
##
##Are you studying well

##creating a file and opening
##d=open(r'Hii.txt','r')
##s=d.readlines()
##a=[]
##for i in s:
##    a.append(i.split(','))
##d.close()
##output:
##a
##[['Hii Jogendra\n'], ['How are you\n'], ['Are you studying well']]

##creating a file and opening
d=open(r'cars.csv','r')
s=d.readlines()
a=[]
for i in s:
    a.append(i.split(','))
d.close()
c=0
for i in a:
    if i[-1]=='us\n':
        c=c+1
print(c)
##output:









































