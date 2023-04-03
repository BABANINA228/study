# 4  from tkinter import *
from tkinter import *

root = Tk()
l = Label(font = 35)
def phone(a, n):
    l.config(text = a)
    if n == 1:
        r1.config(bg = "black")
        print("Сработало 1")
    elif n ==2:
        r2["bg"] = "black"
        print("Сработало 2")
    elif n ==3:
        r3["bg"] = "black"
        print("Сработало 3")
    # l.delete(0, END)
    # l.insert(0,f'{a}')
root.geometry('400x300+200+100')
r1 = Radiobutton(root, height=2, width=5, text = "Вася", indicatoron=0, command = lambda: phone('8-800-55-35-35', 1), activebackground="gray")
r2 = Radiobutton(root, height=2, width=5, text = 'Петя', indicatoron=0, command = lambda: phone('+7978-064-06-24', 2), activebackground="gray")
r3 = Radiobutton(root, height=2, width=5, text = 'Миша', indicatoron=0, command = lambda: phone('Нет номера', 3), activebackground="gray")

l.pack()
r1.pack(anchor=W)
r2.pack(anchor=W)
r3.pack(anchor=W)

root.mainloop()