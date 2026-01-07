#import tkinter
from tkinter import *
#creating main window
r = Tk()
r.geometry("500x500")
r.title("Student System")
r.configure(bg="yellow")
#adding widget into window
tn = Label(r,text="Roll Number",bg="white")
tn.place(x=20,y=20)
tf = Label(r,text="First Name",bg="white")
tf.place(x=20,y=60)
tl = Label(r,text="Last Name",bg="white")
tl.place(x=20,y=100)
te = Label(r,text="Email",bg="white")
te.place(x=20,y=140)
#adding entry box into main window
ern = Entry()
ern.place(x = 100, y=20)
ern = Entry()
ern.place(x = 100, y=60)
ern = Entry()
ern.place(x = 100, y=100)
ern = Entry()
ern.place(x = 100, y=140)
#adding button into main window
button1=Button(r,text = "Button", bg="white")
button1.place(x=20,y=200)
mainloop()
