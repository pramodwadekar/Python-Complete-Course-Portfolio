from tkinter import *
r = Tk()
r.geometry("800x500")
r.title("Windows Setup")
r.configure(bg="blue")

tn = Label(r,text = "Window Server 2016",bg='blue',foreground="white",font='ar 20')
tn.place(x=250,y=30)

tl = Label(r,text="Language to install : ",bg='blue',foreground="white",font="30")
OptionMenu(r, tl, 'English', "Hindi","Marathi").place(x=350,y=150 ,rely=0.001, relwidth=0.16)
tl.place(x=100,y=150)

time = Label(r,text="Time and Currancy Format : ",bg='blue',foreground="white",font="30")
time.place(x=100,y=200)

keybord = Label(r,text="Keybord and Inpute Method : ",bg='blue',foreground="white",font="30")
keybord.place(x=100,y=250)

next = Label(r,text="Enter Your Language and Other preferance and click ""'Next'"" to continue.",bg='blue',foreground="white",font="30")
next.place(x=140,y=350)

cororation = Label(r,text="@ 2016 Microsoft Corporation. All rights reserved.",bg='blue',foreground="white",font="30")
cororation.place(x=50,y=425)


ern = Entry()
ern.place(x=350,y=200)
ern = Entry()
ern.place(x=350,y=250)

button1 = Button(r,text = "Next", border=8)
button1.place(x=700,y=390)
mainloop()