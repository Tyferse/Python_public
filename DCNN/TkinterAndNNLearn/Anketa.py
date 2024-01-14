import tkinter as tk


window = tk.Tk()

window.columnconfigure(0, minsize=20)

lbl1 = tk.Label(text='Имя:', fg='black')
lbl1.grid(row=0, column=0, sticky='e')
lbl2 = tk.Label(text='Фамилия:', fg='black')
lbl2.grid(row=1, column=0, sticky='e')
lbl3 = tk.Label(text='Адрес 1:', fg='black')
lbl3.grid(row=2, column=0, sticky='e')
lbl4 = tk.Label(text='Адрес 2:', fg='black')
lbl4.grid(row=3, column=0, sticky='e')
lbl5 = tk.Label(text='Город:', fg='black')
lbl5.grid(row=4, column=0, sticky='e')
lbl6 = tk.Label(text='Регион:', fg='black')
lbl6.grid(row=5, column=0, sticky='e')
lbl7 = tk.Label(text='Почтовый индекс:', fg='black')
lbl7.grid(row=6, column=0, sticky='e')
lbl8 = tk.Label(text='Страна:', fg='black')
lbl8.grid(row=7, column=0, sticky='e')

# Создание 8-ми полей ввода текста
for i in range(8):
    tk.Entry(width=50).grid(row=i, column=1, pady=1)

frm_b = tk.Frame(relief=tk.RAISED, borderwidth=3)
frm_b.grid(row=8, column=0, columnspan=2, sticky='we')

btn1 = tk.Button(text='Отправить', width=14, height=1, master=frm_b)
btn1.pack(side='right', padx=5, pady=5)

btn2 = tk.Button(text='Очистить', width=10, height=1, master=frm_b)
btn2.pack(side='right', padx=5, pady=5)

window.mainloop()
