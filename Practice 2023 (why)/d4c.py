import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
screen.fill(pg.Color('black'))
pg.display.flip()

screen2 = pg.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
running = True
drawing = False
rectlist = []
rect = tuple()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
            
        if event.type == pg.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            drawing = False
            rectlist.append(rect)
        
        if event.type == pg.MOUSEMOTION:
            w, h = event.pos[0] - x1, event.pos[1] - y1
        
        screen.fill(pg.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:
            if w > 0 and h > 0:
                rect = (x1, y1, w, h)
            elif w < 0 < h:
                rect = (x1 + w, y1, -w, h)
            elif h < 0 < w:
                rect = (x1, y1 + h, w, -h)
            elif h < 0 and w < 0:
                rect = (x1 + w, y1 + h, -w, -h)
            
            pg.draw.rect(screen, (250, 250, 250), rect, 3)
        
        if event.type == pg.KEYDOWN:
            print(event.mod, pg.KMOD_LCTRL)
            if event.key == pg.K_z and event.mod == pg.KMOD_LCTRL:
                # print(len(rectlist), repr(rect))
                if rectlist:
                    screen.fill((0, 0, 0))
                    rectlist = rectlist[:-1]
                    for r in rectlist:
                        pg.draw.rect(screen, (255, 255, 255), r, 3)
                    
                    screen2.blit(screen, (0, 0))
        
    pg.display.flip()

pg.quit()
