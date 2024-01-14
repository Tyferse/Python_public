import tkinter as tk


window = tk.Tk()

"""
# Создает обработчик событий
def handle_keypress(event):
    # Выводит символ, связанный с нажатой клавишей
    print(event.char)


# Связывает событие нажатия клавиши с handle_keypress()
window.bind("<Key>", handle_keypress)
"""

"""
def handle_click(event):
    print("Нажата кнопка!")


button = tk.Button(text="Кликни!")
button.bind("<Button-1>", handle_click)
button.pack()
"""

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)


def increase():
    """Прибавляет к значению числа в метке единицу."""
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    """Отнимает от значения числа в метке единицу."""
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


# Кнопка уменьшения значения в метке
btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

# Метка с числом
lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

# Кнопка увеличения значения в метке
btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
