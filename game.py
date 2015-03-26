#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Outer wrapper script for game.

import sys
import pygame
from terrain import Terrain, colors

pygame.init()
board_size = width, height = 718, 480
tile_size = 24
visibility = 1

screen = pygame.display.set_mode(board_size)
screen.fill(colors['light gray'])

t = Terrain(width, height, tile_size)
for row in t.terrain:
    for tile in row:
        screen.blit(tile.get_surface(),tile.get_position())
pygame.display.flip()
sqY = len(t.terrain)
sqX = len(t.terrain[0])

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


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (cuX,cuY) = pygame.mouse.get_pos()
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
            for tile in current:
                screen.blit(tile.get_surface(),tile.get_position()) # surrounding tiles
            screen.blit(me, coords(myX,myY))  # blit me
            pygame.display.flip()


#sys.exit()
#    elif event.type == pygame.MOUSEBUTTONDOWN: greencube.fill(white)
#    elif event.type == pygame.MOUSEBUTTONUP: greencube.fill(green)

