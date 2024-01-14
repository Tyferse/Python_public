import pygame as pg
from math import pi, sin, cos
from random import randint

pg.init()
size = (600, 600)
screen = pg.display.set_mode(size)

all_sprites = pg.sprite.Group()
sprite = pg.sprite.Sprite()
clock = pg.time.Clock()
fps = 30

horizontal_borders = pg.sprite.Group()
vertical_borders = pg.sprite.Group()


class Border(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pg.Surface((1, y2 - y1))
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pg.Surface((x2 - x1, 1))
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


class Ball(pg.sprite.Sprite):
    def __init__(self, radius, x, y, flag=False):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pg.Surface((2 * radius, 2 * radius),
                                pg.SRCALPHA, 32)
        pg.draw.circle(self.image, pg.Color("red"),
                       (radius, radius), radius)
        self.rect = pg.Rect(x, y, 2 * radius - 5, 2 * radius - 5)
        
        self.speed = randint(10, 25)
        self.vx = round(self.speed *
                        cos(pi * randint(0, 360) / 180))
        self.vy = round(self.speed *
                        sin(pi * randint(0, 360) / 180))
        self.vx = self.vx + 1 if self.vx == 0 else self.vx
        self.vy = self.vy + 1 if self.vy == 0 else self.vy
        
        self.flag = flag
        self.x = x
        self.y = y

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.vx = -self.vx
            
        if pg.sprite.spritecollideany(self, vertical_borders):
            self.vy = -self.vy

        all_sp_buff = all_sprites.copy()
        all_sp_buff.remove(self)
        # if self.flag:
        #     self.vy = -self.vy
        #     self.vx = -self.vx
        #     self.x += 2 * self.radius * (self.vx // abs(self.vx))
        #     self.y += 2 * self.radius * (self.vy // abs(self.vy))
        #     self.rect = pg.Rect(self.x, self.y,
        #                         2 * self.radius - 5,
        #                         2 * self.radius - 5)
        #     self.flag = False
        
        other_sphere_col = pg.sprite.spritecollide(self,
                                                   all_sp_buff, 0)
        if other_sphere_col:
            # self.flag = True
            self.vy = -self.vy
            self.vx = -self.vx
            if isinstance(other_sphere_col[0], Ball):
                self.vy += other_sphere_col[0].vx
                self.vx += other_sphere_col[0].vy
                
                tmplen = (self.vx**2 + self.vy**2)**.5
                self.vx = self.speed * self.vx / tmplen
                self.vy = self.speed * self.vy / tmplen
                # self.flag = True


Border(5, 5, size[0] - 5, 5)
Border(5, size[1] - 5, size[0] - 5, size[1] - 5)
Border(5, 5, 5, size[1] - 5)
Border(size[0] - 5, 5, size[0] - 5, size[1] - 5)

# all_sprites = pg.sprite.Group()
for _ in range(5):
    Ball(20, randint(25, size[0] - 25),
         randint(25, size[1] - 25), True)

running = True
while running:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            Ball(20, *pos)

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.flip()
    clock.tick(fps)

pg.quit()
