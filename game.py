#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Outer wrapper script for game.

import sys
import pygame
from terrain import Terrain, colors

pygame.init()
board_size = width, height = 720, 528
score_panel = 168
tile_size = 24
visibility = 1
timer = 5 * 60   #seconds

screen = pygame.display.set_mode((width+score_panel,height))
screen.fill(colors['light gray'])

t = Terrain(width, height, tile_size)
for row in t.terrain:
    for tile in row:
        screen.blit(tile.get_surface(),tile.get_position())
pygame.display.flip()
sqY = len(t.terrain)
sqX = len(t.terrain[0])

### set up score panel ###
s = 10
w = width + s
h = s

if not pygame.font.get_init(): sys.exit("missing font module")
text = pygame.font.SysFont('Arial',20)
inc = text.get_linesize()
tcolor = colors['black']

tscore = text.render(u'Score',True,tcolor)
screen.blit(tscore,(w,h))
scorebox = pygame.Surface((50,inc))
scorebox.fill((210,210,210))
scorepos = (w+tscore.get_width()+s,h)
screen.blit(scorebox,scorepos)
tclock = text.render(u'Time Remaining',True,tcolor)
screen.blit(tclock,(w,h+s+inc))
clockbox = pygame.Surface((80,inc))
clockbox.fill((210,210,210))    #colors['light gray'])
clockpos = (w+s,h+2*s+2*inc)
screen.blit(clockbox,clockpos)
tbasket = text.render(u'My Basket',True,tcolor)
screen.blit(tbasket,(w,4*h+3*inc))
tgather = text.render(u'Gather',True,tcolor)
screen.blit(tgather,(w,8*h+7*inc))
### ###

def update_screentime(last):
    millisecs = pygame.time.get_ticks()
    if millisecs-last > 1000:
        stime = (timer*1000 - millisecs) / 1000
        screentime = text.render(str(stime),True,tcolor)
        screen.blit(clockbox,clockpos)
        screen.blit(screentime,clockpos)
        pygame.display.flip()
        return millisecs
    else:
        return last

me = pygame.Surface((tile_size,tile_size))
me.fill((0,0,0))
me.fill(colors['yellow'],(tile_size/4,tile_size/4,tile_size/2,tile_size/2))
me.set_colorkey((0,0,0))

fog = pygame.Surface((tile_size,tile_size))
fog.fill(colors['black'])
fog.set_alpha(125)

def coords(i,j):
    return (i*tile_size,j*tile_size)

def visible(X,Y,V):
    current = []
    for x in range(X-V, X+V+1):
        for y in range(Y-V, Y+V+1):
            if x<0 or x>=sqX: continue
            if y<0 or y>=sqY: continue
            t.terrain[y][x].make_visible()
            current.append(t.terrain[y][x])
    return current

myX = width/tile_size/2
myY = height/tile_size/2
current = visible(myX,myY,visibility)
for tile in current:
    screen.blit(tile.get_surface(),tile.get_position()) # surrounding tiles
screen.blit(me, coords(myX,myY))
pygame.display.flip()

clock = pygame.time.Clock()
ticker = 0

while 1:
    clock.tick(10) # limits the while loop to a max of 10 times per second
    ticker = update_screentime(ticker)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (cuX,cuY) = pygame.mouse.get_pos()
            if cuX >= width:
                pass
            elif cuX == myX and cuY == myY:
                pass#pick flower
            elif cuX < width and cuY < height:
                for tile in current:
                    surf = tile.get_surface()
                    pos = tile.get_position()
                    screen.blit(surf,pos) # blit background
                    screen.blit(fog,pos)
                if cuX/tile_size < myX: myX = myX - 1
                if cuX/tile_size > myX: myX = myX + 1
                if cuY/tile_size < myY: myY = myY - 1
                if cuY/tile_size > myY: myY = myY + 1
                current = visible(myX,myY,visibility)
                for tile in current: # blit surrounding tiles
                    screen.blit(tile.get_surface(),tile.get_position()) 
                screen.blit(me, coords(myX,myY))  # blit me
                pygame.display.flip()


#sys.exit()
#    elif event.type == pygame.MOUSEBUTTONDOWN: greencube.fill(white)
#    elif event.type == pygame.MOUSEBUTTONUP: greencube.fill(green)

