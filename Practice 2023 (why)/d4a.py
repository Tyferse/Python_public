import pygame as pg

w, n = map(int, input().split())
pg.init()
screen = pg.display.set_mode((w, w))

screen.fill((255, 255, 255))

for y in range(w // n):
    for x in range(y % 2, w // n, 2):
        pg.draw.rect(screen, (0, 0, 0), (x * n, y * n, n, n))

pg.display.flip()

while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()
