import tkinter as tk
import random


def gennum():
    """Меняет текст метки lbl на случайное число от 1 до 6."""
    num = random.randint(1, 6)
    lbl['text'] = str(num)


window = tk.Tk()

window.columnconfigure(0, minsize=150, weight=1)
window.rowconfigure([0, 1], minsize=100, weight=1)

# Кнопка, изменяющая значение в метке
btn = tk.Button(text='Бросить', fg='black', command=gennum,
                master=window)
btn.grid(column=0, row=0, ipadx=5, ipady=10, sticky='nswe')

frm = tk.Frame(master=window)
frm.grid(column=0, row=1)
lbl = tk.Label(text='0', master=frm)
lbl.pack(ipady=10, fill='both')

window.mainloop()
