import pygame as pg
import random


pg.init()
size = (600, 600)
screen = pg.display.set_mode((600, 600))

all_sprites = pg.sprite.Group()
sprite = pg.sprite.Sprite()
clock = pg.time.Clock()
fps = 60


class Ball(pg.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pg.Surface((2 * radius, 2 * radius),
                                    pg.SRCALPHA, 32)
        pg.draw.circle(self.image, pg.Color("red"),
                           (radius, radius), radius)
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
    
    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pg.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


# Функция spritecollideany() возвращает спрайт из группы, с которым произошло столкновение или None,
# если столкновение не обнаружено.
# Другая функция, spritecollide(), принимает в качестве аргументов так же спрайт и группу — возвращает список
# спрайтов из группы, с которыми произошло пересечение.
# Третьим параметром можно передать логическое значение True, и тогда все спрайты, с которыми есть пересечение,
# будут уничтожены и убраны из группы.

horizontal_borders = pg.sprite.Group()
vertical_borders = pg.sprite.Group()


class Border(pg.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


Border(5, 5, size[0] - 5, 5)
Border(5, size[1] - 5, size[0] - 5, size[1] - 5)
Border(5, 5, 5, size[1] - 5)
Border(size[0] - 5, 5, size[0] - 5, size[1] - 5)

for i in range(10):
    Ball(20, 100, 100)


running = True
while running:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            Ball(20, *pos)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.flip()
    clock.tick(fps)

pg.quit()
