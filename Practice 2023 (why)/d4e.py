import pygame as pg
from math import pi, sin, cos
from random import randint

n = 360
radius = 280
pg.init()
screen = pg.display.set_mode((600, 600))

alive = True
animate = True
c = 2

clr = pg.Color(randint(0, 255),
               randint(0, 255),
               randint(0, 255))
while alive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            alive = False
        
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            animate = not animate
        
    if animate:
        screen.fill((0, 0, 0))
        pg.draw.circle(screen, (255, 255, 255),
                       (screen.get_width() // 2,
                        screen.get_height() // 2),
                       radius, 2)
        # pg.display.flip()
            
        # clr = pg.Color(randint(0, 255),
        #                randint(0, 255),
        #                randint(0, 255))
        for i in range(n):
            clr.hsva = ((clr.hsva[0] + 1.) % 360,
                        (clr.hsva[1] + randint(0, 100)) % 100,
                        clr.hsva[2], clr.hsva[3])
            pg.draw.line(screen, clr,
                         (cos(i * 2 * pi / n) * radius
                          + screen.get_width() // 2,
                          sin(i * 2 * pi / n) * radius
                          + screen.get_height() // 2),
                         (cos(c * i * 2 * pi / n) * radius
                          + screen.get_width() // 2,
                          sin(c * i * 2 * pi / n) * radius
                          + screen.get_height() // 2))
        
        pg.display.flip()
            
        c += 0.001

pg.quit()
