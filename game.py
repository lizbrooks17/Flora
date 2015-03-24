#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Outer wrapper script for game.

import sys
import pygame
from terrain import Terrain

pygame.init()
size = width, height = 700, 500

screen = pygame.display.set_mode(size)
screen.fill((192,192,192))   # light gray

t = Terrain(width, height)
for row in t.terrain:
    for tile in row:
        screen.blit(tile.get_surface(),tile.get_position())
pygame.display.flip()

me = pygame.Surface((20,20))
me.fill((0,0,0))
me.fill((255,255,51),(5,5,10,10))   #yellow
me.set_colorkey((0,0,0))

def coords(i,j):
    return (i*20,j*20)

myX = width/20/2
myY = height/20/2
screen.blit(me, coords(myX,myY))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tile = t.terrain[myY][myX]
            screen.blit(tile.get_surface(),tile.get_position()) # blit background
            cuX,cuY = pygame.mouse.get_pos()
            if cuX/20 < myX: myX = myX - 1
            if cuX/20 > myX: myX = myX + 1
            if cuY/20 < myY: myY = myY - 1
            if cuY/20 > myY: myY = myY + 1
            screen.blit(me, coords(myX,myY))  # blit me
            pygame.display.flip()


#sys.exit()
#    elif event.type == pygame.MOUSEBUTTONDOWN: greencube.fill(white)
#    elif event.type == pygame.MOUSEBUTTONUP: greencube.fill(green)
