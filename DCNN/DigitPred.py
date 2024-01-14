import tkinter as tk
from PIL import Image, ImageGrab
import numpy as np
from keras import models


__version__ = '1.0'

# Загрузка модели (нейросети)
model = models.load_model('trained_model.h5')

"""
pyinstaller --onefile -w "C:\Code\Python3\DCNN\DigitPred.py"
"""


def result(file):
    """Возвращает результат предсказания по введённому изображению."""
    # Конвертирование в чёрно-белое изображение
    img0 = Image.open(file).convert("L")
    # Преобразование изображения в массив (матрицу) чисел
    # указанного типа
    image_np = np.asarray(img0, dtype='uint8')
    # Уменьшение размера изображения в 10 раз по ширине и длине
    image_np = np.reshape(image_np, (1, 28, 28))
    prediction = model.predict(image_np)[0]
    lst = []
    # Формирование результата вывода для UI в виде списка строк
    for i in range(10):
        if prediction[i] > 0.:
            res = f'{i} = {prediction[i] * 100: .2f}%'
            lst.append(res)
            
    return lst
    

"""
# Тестирование на заранее подготовленных изображениях
for x in range(10):
    f = 'TestImages\\testimg' + str(x) + '.png'
    print('\n', f)
    print_result(f)
"""


class Paint(tk.Frame):
    """Предназначен для генерирования "холста" для рисования."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Параметры кисти по умолчанию
        self.brush_size = 7
        self.brush_color = "white"
        self.color = "white"
        
        #
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
        global start_btn

        # Устанавливаем название окна
        self.parent.title("Распознаватель цифр " + __version__)
        self.pack(fill=tk.BOTH)

        # self.columnconfigure(6, weight=1)
        # self.rowconfigure(2, weight=1)

        #
        self.canv = tk.Canvas(self, bg="black", relief=tk.SUNKEN, bd=8,
                              height=270, width=270)
        self.canv.grid(row=0, column=0, columnspan=7, padx=5, pady=5)
        self.canv.bind("<B1-Motion>", self.draw)

        color_lab = tk.Label(self, text="Редактирование: ")
        color_lab.grid(row=2, column=0, padx=6)

        black_btn = tk.Button(self, text="\"Ластик\"", width=7,
                              command=lambda: self.set_color("black"))
        black_btn.grid(row=2, column=2)

        white_btn = tk.Button(self, text="Кисть", width=7,
                              command=lambda: self.set_color("white"))
        white_btn.grid(row=2, column=1)

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

        #
        start_btn = tk.Button(self, text='Запуск', width=8, height=3,
                              relief=tk.RAISED, borderwidth=3,
                              font='bold 18', bg='red3',
                              activebackground='red')
        # start_btn.bind('<Button-1>', _snapsaveCanvas)
        start_btn.grid(row=3, column=0, columnspan=4, rowspan=2,
                       pady=30)
        
        self.canv.winfo_height()
        
    # def _canvas(self):
    #     """Получение координат холста."""
    #     # x = self.canv.winfo_rootx() # + 4
    #     # y = self.canv.winfo_rooty() # + 4
    #     # x1 = x + self.canv.winfo_width() # - 10
    #     # y1 = y + self.canv.winfo_height() # - 10
    #     # x = self.canv.winfo_rootx() + self.canv.winfo_x()
    #     # y = self.canv.winfo_rooty() + self.canv.winfo_y()
    #     # x1 = x + self.canv.winfo_width()
    #     # y1 = y + self.canv.winfo_height()
    #     # box = (x, y, x1, y1)
    #
    #     # после создания нашего PS
    #     self.canv.postscript(file="TestImages\out_snapsave.ps",
    #                          colormode="color")
    #
    #     # преобразовываем в PNG
    #     img = Image.open("TestImages\out_snapsave.ps")
    #     img.save("TestImages\out_snapsave.png")


def main():
    global root
    
    root = tk.Tk()
    app = Paint(root)
    # root.geometry('400x600')

    bdthickness_bd = 2
    hlthickness = 1

    def save(stageframe, stage, savelocation="TestImages\\"
                                             "out_snapsave.png"):
        nonlocal bdthickness_bd, hlthickness
        brdt = bdthickness_bd + hlthickness
        # +1 and -2 because of thicknesses of Canvas borders
        # (bd-border and highlight-border):
        # x = root.winfo_rootx() + stageframe.winfo_x() \
        #                        + stage.winfo_x() + 1 * brdt
        # y = root.winfo_rooty() + stageframe.winfo_y() \
        #                        + stage.winfo_y() + 1 * brdt
        # x1 = x + stage.winfo_width() - 2 * brdt
        # y1 = y + stage.winfo_height() - 2 * brdt
        x = stage.winfo_rootx() + 8
        y = stage.winfo_rooty() + 8
        x1 = x + stage.winfo_width()
        y1 = y + stage.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(savelocation)
        
    def _snapsaveCanvas(event):
        # ImageGrab.grab(bbox=app._canvas())
        #          .save('TestImages\\out_snapsave.png')

        save(app, app.canv)
        img = Image.open('TestImages\\'
                         'out_snapsave.png').resize((28, 28))
        img.save('TestImages\in_snapsave.png')

        answerlist = result('TestImages\in_snapsave.png')

        start_btn.destroy()
        txt1 = 'Скорее всего,\nэто цифра:' if len(answerlist) == 1 \
            else 'Скорее всего,\n это одна из цифр:'
        top_lbl = tk.Label(text=txt1, master=app, font='24')
        top_lbl.grid(row=3, column=0, columnspan=4, pady=15)
        res_lbls = []
        lastrow = 3
        for i in range(len(answerlist)):
            ans_lbl = tk.Label(text=answerlist[i], font='36',
                               master=app)
            ans_lbl.grid(row=4 + i, column=0, columnspan=4, pady=5)
            res_lbls.append(ans_lbl)
            lastrow = 4 + i

        def reset_result(event):
            global start_btn
            reset_btn.destroy()
            for lbl in res_lbls:
                lbl.destroy()

            top_lbl.destroy()

            start_btn = tk.Button(app, text='Запуск', width=8, height=3,
                                  relief=tk.RAISED, borderwidth=3,
                                  font='bold 18', bg='red3',
                                  activebackground='red')
            # start_btn.bind('<Button-1>', _snapsaveCanvas)
            start_btn.grid(row=3, column=0, columnspan=4, rowspan=2,
                           pady=30)
            start_btn.bind('<Button-1>', _snapsaveCanvas)

        reset_btn = tk.Button(text='Попробовать заново', master=app)
        reset_btn.grid(row=lastrow + 1, column=0, columnspan=4, pady=5)
        reset_btn.bind('<Button-1>', reset_result)

    start_btn.bind('<Button-1>', _snapsaveCanvas)

    root.mainloop()


if __name__ == "__main__":
    main()
