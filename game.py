#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Outer wrapper script for game.

import sys
import pygame
from terrain import Terrain, colors
from panel import Sidepanel, Basket

pygame.init()
board_size = width, height = 720, 528
panelwidth = 168
tile_size = 24
visibility = 1
timer = 5 * 60   #seconds

screen = pygame.display.set_mode((width+panelwidth,height))
screen.fill(colors['light gray'])

### set up map board ###
board = Terrain(width, height, tile_size)
for row in board.terrain:
    for tile in row:
        screen.blit(tile.get_surface(),tile.get_position())
pygame.display.flip()
sqY = len(board.terrain)
sqX = len(board.terrain[0])

### set up score panel ###
side = Sidepanel(panelwidth,height,colors['light gray'])
screen.blit(side.get_surface(),(width,0))
pygame.display.flip()

def pick_flower(X,Y):
    tile = board.terrain[Y][X]
    flower = tile.get_flower() # color triple for now, later image or surf
    if flower:
        if not basket.add_flower(flower): print 'Basket Full'

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
            board.terrain[y][x].make_visible()
            current.append(board.terrain[y][x])
    return current

myX = width/tile_size/2
myY = height/tile_size/2
current = visible(myX,myY,visibility)

def redrawme():
    for tile in current:
        screen.blit(tile.get_surface(),tile.get_position()) 
    screen.blit(me, coords(myX,myY))
    pygame.display.flip()

redrawme()

clock = pygame.time.Clock()
ticker = 0

while 1:
    clock.tick(10) # limits the while loop to a max of 10 times per second
    #DEBUG ticker = update_screentime(ticker)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (cuX,cuY) = pygame.mouse.get_pos()
            if cuX >= width:
                pass
            elif cuX/tile_size == myX and cuY/tile_size == myY:
                pick_flower(myX,myY)
                redrawme()
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
                redrawme()


#sys.exit()
#    elif event.type == pygame.MOUSEBUTTONDOWN: greencube.fill(white)
#    elif event.type == pygame.MOUSEBUTTONUP: greencube.fill(green)

