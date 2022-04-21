from tkinter import *
from tkinter import messagebox
def hienthi():
    hoten=ten.get()
    matkhau=mk.get()
    if (hoten=='nguyendudung' and matkhau=='0386534771'):
        messagebox.showinfo('Thông báo','Thông tin đúng!')
    else:
        messagebox.showerror('Thông báo','Thông tin sai!')
        
win = Tk ()
win.geometry('250x90+300+300')

Label(win,text="  Ten").grid(row=0, column=0)
Label(win,text="  Mat khau").grid(row=1, column=0)
Button (win, text = "Xac nhan",command=hienthi).grid(row=2, column=0)

ten=Entry(win)
mk=Entry(win)
ten.grid(row=0, column=2)
mk.grid(row=1, column=2)
ten.insert(0,"Ho ten")
mk.insert(0,"Mat khau")
ten.focus()



win.mainloop()
