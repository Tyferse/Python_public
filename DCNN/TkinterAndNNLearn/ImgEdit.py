import tkinter as tk
# from tkinter import messagebox
# import PIL
from PIL import ImageGrab, Image


class Paint(tk.Frame):
    """Предназначен для генерирования "холста" для рисования."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        # Параметры кисти по умолчанию
        self.brush_size = 7
        self.brush_color = "white"
        self.color = "white"
        
        # Устанавливаем компоненты UI
        self.setUI()

    def draw(self, event):
        """Метод рисования на холсте."""
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def set_color(self, new_color):
        """Изменение цвета кисти."""
        self.color = new_color

    def set_brush_size(self, new_size):
        """Изменение размера кисти."""
        self.brush_size = new_size

    def setUI(self):
        """Создание начального графического интерфейса."""
        
        # Устанавливаем название окна
        self.parent.title("Распознаватель цифр")
        # Размещаем активные элементы на родительском окне
        self.pack(fill=tk.BOTH)

        # self.columnconfigure(6, weight=1)
        # self.rowconfigure(2, weight=1)

        # Создаем холст с чёрным фоном
        self.canv = tk.Canvas(self, bg="black", relief=tk.SUNKEN, bd=8,
                              height=270, width=270)

        # Прикрепляем холст методом grid.
        # Он будет находиться в 0-м ряду, нулевой колонке,
        # и будет занимать 7 колонок,
        # задаем отступы по X и Y в 5 пикселей
        self.canv.grid(row=0, column=0, columnspan=7, padx=5, pady=5)

        # Задаем реакцию холста на нажатие левой кнопки мыши
        self.canv.bind("<B1-Motion>", self.draw)

        # Создаем метку для кнопок изменения цвета кисти
        color_lab = tk.Label(self, text="Редактирование: ")

        # Устанавливаем созданную метку во второй ряд и нулевую колонку,
        # задаем горизонтальный отступ в 6 пикселей
        color_lab.grid(row=2, column=0, padx=6)

        black_btn = tk.Button(self, text="\"Ластик\"", width=7,
                              command=lambda: self.set_color("black"))
        black_btn.grid(row=2, column=2)

        white_btn = tk.Button(self, text="Кисть", width=7,
                              command=lambda: self.set_color("white"))
        white_btn.grid(row=2, column=1)

        # Создаем метку для кнопок изменения размера кисти
        size_lab = tk.Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)

        two_btn = tk.Button(self, text="4x", width=7,
                            command=lambda: self.set_brush_size(4))
        two_btn.grid(row=1, column=1)
        three_btn = tk.Button(self, text="7x", width=7,
                              command=lambda: self.set_brush_size(7))
        three_btn.grid(row=1, column=2)
        four_btn = tk.Button(self, text="10x", width=7,
                             command=lambda: self.set_brush_size(10))
        four_btn.grid(row=1, column=3)

        clear_btn = tk.Button(self, text="Очистить", width=7,
                              command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=2, column=3)

        # Кнопка запуска распознавания цифр (для теста)
        start_btn = tk.Button(self, text='Запуск', width=8, height=3,
                              relief=tk.RAISED, borderwidth=3,
                              font='bold 18', bg='red3',
                              activebackground='red')
        start_btn.bind('<Button-1>', self._snapsaveCanvas)
        start_btn.grid(row=3, column=0, columnspan=4, rowspan=2,
                       pady=30)

    def _snapsaveCanvas(self, event):
        """Сохранение изображения холста."""
        canvas = self._canvas()  # Получаем координаты холста
        ImageGrab.grab(bbox=canvas).save('C:\Code\Python3\DCNN\\'
                                         'TestImages\out_snapsave.png')
        img = Image.open('C:\Code\Python3\DCNN\\'
                         'TestImages\out_snapsave.png').resize((28, 28))
        img.save('C:\Code\Python3\DCNN\\TestImages\in_snapsave.png')

    def _canvas(self):
        """Получение координат холста."""

        # print('self.cv.winfo_rootx() = ', self.canv.winfo_rootx())
        # print('self.cv.winfo_rooty() = ', self.canv.winfo_rooty())
        # print('self.cv.winfo_x() =', self.canv.winfo_x())
        # print('self.cv.winfo_y() =', self.canv.winfo_y())
        # print('self.cv.winfo_width() =', self.canv.winfo_width())
        # print('self.cv.winfo_height() =', self.canv.winfo_height())
        
        x = self.canv.winfo_rootx() + 4
        # + 2  # + self.canv.winfo_x()
        y = self.canv.winfo_rooty() + 4
        # + 2 # + self.canv.winfo_y()
        x1 = x + self.canv.winfo_width() - 8 - 2
        # - 8 # - self.canv.winfo_x()
        y1 = y + self.canv.winfo_height() - 8 - 2
        # - 8 # - self.canv.winfo_y()
        
        box = (x, y, x1, y1)
        print('box = ', box)
        return box


def main():
    """Функция для создания главного окна"""
    global root
    root = tk.Tk()
    # root.geometry("300x450")
    app = Paint(root)

    root.mainloop()


if __name__ == "__main__":
    main()
