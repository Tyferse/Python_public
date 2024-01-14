import pygame as pg
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self._generated = False
        
        self.left = 25
        self.top = 25
        self.cell_size = 55
    
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def render(self, scr):
        for y in range(self.height + 1):
            pg.draw.line(scr, (250, 250, 250),
                         (self.left, self.top + y * self.cell_size),
                         (self.left + self.width * self.cell_size,
                          self.top + y * self.cell_size), 3)
        
        for x in range(self.width + 1):
            pg.draw.line(scr, (250, 250, 250),
                         (self.left + x * self.cell_size, self.top),
                         (self.left + x * self.cell_size,
                          self.top + self.height * self.cell_size), 3)
        
        if not self._generated:
            for y in range(self.height):
                for x in range(self.width):
                    if randint(0, 100) \
                       <= 25:
                        self.board[y][x] = -1
                        for i in (-1, 0, 1):
                            for j in (-1, 0, 1):
                                if (0 <= x + i < self.width
                                   and 0 <= y + j < self.height) \
                                   and self.board[y + j][x + i] != -1:
                                    self.board[y + j][x + i] += 1
            
            self._generated = True
        
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    pg.draw.rect(
                        scr, (235, 10, 10),
                        (self.left + 2 + x * self.cell_size,
                         self.top + 2 + y * self.cell_size,
                         self.cell_size - 3, self.cell_size - 3)
                    )
                elif self.board[y][x] > 9:
                    font = pg.font.Font(None, 36)
                    text = font.render(str(self.board[y][x] - 10),
                                       True, (0, 190, 235))
                    text_x = self.left + 8 + x * self.cell_size
                    text_y = self.top + 8 + y * self.cell_size
                    screen.blit(text, (text_x, text_y))
    
    def get_cell(self, scr, pos: tuple):
        x, y = pos
        if x < self.left \
           or x > self.width * self.cell_size + self.left \
           or y < self.top \
           or y > self.height * self.cell_size + self.top:
            return None
    
        row = (x - self.left) // self.cell_size
        column = (y - self.top) // self.cell_size
        return row, column
    
    def on_click(self, coords):
        x, y = coords
        if -1 < self.board[y][x] < 10:
            self.board[y][x] += 10
    
    def get_click(self, scr, mouse_pos):
        cell = self.get_cell(scr, mouse_pos)
        if cell is None:
            return
        
        self.on_click(cell)


pg.init()
screen = pg.display.set_mode((600, 600))

board = Board(10, 10)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            board.get_click(screen, pg.mouse.get_pos())
            # print(board.get_cell(screen, pg.mouse.get_pos()))
            
    screen.fill((0, 0, 0))
    board.render(screen)
    # print(*board.board, sep='\n', end='\n\n\n')
    pg.display.flip()

pg.quit()
