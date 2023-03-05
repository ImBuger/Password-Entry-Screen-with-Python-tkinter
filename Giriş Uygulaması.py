from tkinter import *

pencere = Tk()

def sign_in():
    password = entry.get()
    Pass = "Utku Buğra Yılmaz"

    if password == Pass.lower() or password == Pass.upper():
        label.config(text = "Enter Succesfull")
        entry.destroy()
        button.destroy()

    else:
        label2 = Label(pencere)
        label2.config(text = "Wrong Password!", font = ("Arial", 10))
        label2.place(x = 20, y = 120)


label = Label(pencere)
label.config(text = "Enter your password:", font = ("Arial",20))
label.place(x = 20,y = 20)

entry = Entry(pencere)
entry.place(x = 20,y = 70)

button = Button(pencere)
button.config(text = "Enter", bg = "black", fg = "white", command = sign_in)
button.place(x = 20,y = 100)
#-_-
mainloop()
