from tkinter import *

class Communal_apartment():
    def __init__(self, pred=0, now=0):
        self.pred = pred
        self.now = now
    @staticmethod
    def count(pred, now, tarif):
        l4.config(text=f"Итого: {round((now-pred)*tarif,2)}")

root = Tk()
rates = [10.3, 17.8, 34.81, 8]
f1 = LabelFrame(width=300, height=200, bg="gray", text="Горячая вода", font=('Times New Roman', 20), borderwidth=3)

l1_f1 = Label(f1, text="Предыдущие показания:", width=24, font=('Times New Roman', 12))
l2_f1 = Label(f1, text="Текущие показания:", width=24, font=('Times New Roman', 12))
e1_f1 = Entry(f1)
e2_f1 = Entry(f1)
l3_f1 = Label(f1, text=f"Тариф: {rates[0]}")
b1 = Button(f1, width=10, height=1, text="Посчитать", command=lambda: Communal_apartment.count(int(e1_f1.get()),int(e2_f1.get()),rates[0]))
l4_f1 = Label(f1, width=15, height=2, text="Итого:  0", justify=LEFT)

l1_f1.grid(row=0, column=0, pady=5)
l2_f1.grid(row=1, column=0, pady=5)
e1_f1.grid(row=0, column=1)
e2_f1.grid(row=1, column=1)
l3_f1.grid(row=2, column=0, pady=5)
b1.grid(row=3, column=0, pady=10)
l4_f1.grid(row=3, column=1)

# l1.pack(anchor=W, pady=10)
# l2.pack(anchor=W)
# e1.pack(anchor=NE)
# e2.pack(anchor=NE)
# b1.pack(side=LEFT)
# l3.pack(side=RIGHT)

# Фрейм 2
f2 = LabelFrame(width=300, height=200, bg="gray", text="Холодная вода", font=('Times New Roman', 20), borderwidth=3)

l1_f2 = Label(f2, text="Предыдущие показания:", width=24, font=('Times New Roman', 12))
l2_f2 = Label(f2, text="Текущие показания:", width=24, font=('Times New Roman', 12))
e1_f2 = Entry(f2)
e2_f2 = Entry(f2)
l3_f2 = Label(f2, text=f"Тариф: {rates[0]}")
b2 = Button(f2, width=10, height=1, text="Посчитать", command=lambda: Communal_apartment.count(int(e1_f2.get()),int(e2_f2.get()),rates[1]))
l4_f2 = Label(f2, width=15, height=2, text="Итого:  0", justify=LEFT)

l1_f2.grid(row=0, column=0, pady=5)
l2_f2.grid(row=1, column=0, pady=5)
e1_f2.grid(row=0, column=1)
e2_f2.grid(row=1, column=1)
l3_f2.grid(row=2, column=0, pady=5)
b2.grid(row=3, column=0, pady=10)
l4_f2.grid(row=3, column=1)

# Фрейм 3
f3 = LabelFrame(width=300, height=200, bg="gray", text="Газ", font=('Times New Roman', 20), borderwidth=3)

l1_f3 = Label(f3, text="Предыдущие показания:", width=24, font=('Times New Roman', 12))
l2_f3 = Label(f3, text="Текущие показания:", width=24, font=('Times New Roman', 12))
e1_f3 = Entry(f3)
e2_f3 = Entry(f3)
l3_f3 = Label(f3, text=f"Тариф: {rates[0]}")
b3 = Button(f3, width=10, height=1, text="Посчитать", command=lambda: Communal_apartment.count(int(e1_f3.get()),int(e2_f3.get()),rates[2]))
l4_f3 = Label(f3, width=15, height=2, text="Итого:  0", justify=LEFT)

l1_f3.grid(row=0, column=0, pady=5)
l2_f3.grid(row=1, column=0, pady=5)
e1_f3.grid(row=0, column=1)
e2_f3.grid(row=1, column=1)
l3_f3.grid(row=2, column=0, pady=5)
b3.grid(row=3, column=0, pady=10)
l4_f3.grid(row=3, column=1)

# Фрейм 4
f4 = LabelFrame(width=300, height=200, bg="gray", text="Электроэнергия", font=('Times New Roman', 20), borderwidth=3)

l1_f4 = Label(f4, text="Предыдущие показания:", width=24, font=('Times New Roman', 12))
l2_f4 = Label(f4, text="Текущие показания:", width=24, font=('Times New Roman', 12))
e1_f4 = Entry(f4)
e2_f4 = Entry(f4)
l3_f4 = Label(f4, text=f"Тариф: {rates[0]}")
b4 = Button(f4, width=10, height=1, text="Посчитать", command=lambda: Communal_apartment.count(int(e1_f4.get()),int(e2_f4.get()),rates[3]))
l4_f4 = Label(f4, width=15, height=2, text="Итого:  0", justify=LEFT)

l1_f4.grid(row=0, column=0, pady=5)
l2_f4.grid(row=1, column=0, pady=5)
e1_f4.grid(row=0, column=1)
e2_f4.grid(row=1, column=1)
l3_f4.grid(row=2, column=0, pady=5)
b4.grid(row=3, column=0, pady=10)
l4_f4.grid(row=3, column=1)

l =Label(text="Сумма к оплате", font=(('Times New Roman', 24)), relief=GROOVE)

f1.grid(row=0, column=0)
f2.grid(row=0, column=1, padx=10)
f3.grid(row=0, column=2, padx=10)
f4.grid(row=0, column=3)
l.grid(row=1, column=0, columnspan=4)
root.mainloop()