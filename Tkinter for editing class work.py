##Editing
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Button(a,text='submit',fg='green',bg='orange')
##b.pack(side='bottom')
##b=tk.Button(a,text='cancel',fg='yellow',bg='blue')
##b.pack(side='bottom')
####bottom , top , left , right
##a.mainloop()

####Editing
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Button(a,text='submit',fg='blue',bg='pink')
##b.grid(row=0,column=0)
##c=tk.Button(a,text='cancel',fg='red',bg='cyan')
##c.grid(row=1,column=0)
##a.mainloop()

##Button submit and cancel
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Button(a,text='submit',fg='blue',bg='pink')
##b.place(x=10,y=10)
##c=tk.Button(a,text='cancel',fg='red',bg='cyan')
##c.place(x=100,y=10)
##a.mainloop()

##Labels
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Label(a,text='username',fg='blue',bg='orange')
##b.grid(row=0,column=0)
##d=tk.Entry()
##d.grid(row=0,column=1)
##c=tk.Label(a,text='password',fg='red',bg='navy')
##c.grid(row=1,column=0)
##e=tk.Entry()
##e.grid(row=1,column=1)
##a.mainloop()

####Checkbutton
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Checkbutton(a,text='python',fg='blue',bg='orange')
##b.grid(row=0,column=0)
##b=tk.Checkbutton(a,text='HTML',fg='blue',bg='pink')
##b.grid(row=1,column=0)
##a.mainloop()


##Dropbox
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Listbox()
##b.insert(1,'C')
##b.insert(2,'Cpp')
##b.insert(3,'Data structures through c')
##b.insert(4,'Python')
##b.insert(5,'Java')
##b.insert(6,'HTML')
##b.insert(7,'CSS')
##b.insert(8,'Java script')
##b.insert(9,'objected oriented programming')
##b.insert(10,'Pega')
##b.pack()
##a.mainloop()

####Spin box
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##b=tk.Spinbox(a,from_=1,to=20,fg='blue',bg='orange')
##b.grid(row=0,column=0)
##a.mainloop()

##message Box
##import tkinter as tk
##from tkinter import messagebox
##a=tk.Tk()
##a.title('sample')
##def example():
####    messagebox.showinfo('Hii','Jogendra')
##    messagebox.askquestion('Hii','Jogendra')
##b=tk.Button(a,text='Submit',fg='blue',bg='pink',command=example)
##b.grid(row=0,column=0)
##a.mainloop()

##message Box
##import tkinter as tk
##a=tk.Tk()
##a.title('sample')
##def example():
##    q=int(c.get())
##    w=int(b.get())
##    print(q+w)
##b=tk.Entry()
##b.grid(row=0,column=0)
##c=tk.Entry()
##c.grid(row=0,column=1)
##d=tk.Button(a,text='Submit',fg='blue',bg='orange',command=example)
##d.grid(row=0,column=2)
##a.mainloop()

##import calendar
##year=int(input("Enter the year: "))
##month=int(input("Enter the month: "))
##print(calendar.month(year,month))

##calendar
from tkinter import *
import tkinter as tk
import calendar
r=tk.Tk()
r.geometry('400x300')
r.title('Calendar')

def show():
    m=int(month.get())
    y=int(year.get())
    output=calendar.month(y,m)
    cal.insert('end',output)
def clear():
    cal.delete(1.0,'end')
def exit():
    r.destroy()

m_label=Label(r,text='Month',font=('verdana','10','bold'))
m_label.place(x=70,y=80)

month=Spinbox(r,from_=1,to=12,width="5")
month.place(x=140,y=80)
              
y_label = Label (r, text="Year")
y_label.place (x=210,y=80)

year = Spinbox (r, from_ = 2020, to= 3000, width="8")
year.place (x=260, y=80)

cal = Text (r, width=33, height=8, relief=RIDGE, borderwidth=2)
cal.place (x=70,y=110)

show = Button (r, text="Show", command=show)
show.place (x=140,y=250)
              
clear = Button (r, text="Clear", command=clear)
clear.place (x=200,y=250)

ex=Button(r,text='Exit',command=exit)
ex.place(x=260,y=250)















