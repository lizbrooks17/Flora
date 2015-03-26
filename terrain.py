#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Classes for Tiles and game Board

import pygame
import random

NO = 0
YES = 1
colors = { 'black':(0,0,0),
           'red':(255,0,0),
           'blue':(0,0,255),
           'green':(0,255,0),
           'white':(255,255,255),
           'yellow':(255,255,51),
           'light gray':(192,192,192),
          }

blues = [(102,178,255),(0,128,255),(0,128,255),(0,0,255),(0,0,255),(0,0,153),]

def set_color():
    #color = random.choice(colors.keys())
    #return colors[color]
    color = random.choice(blues)
    return color

def set_flower():
    return None

class Tile:
    def __init__(self,X,Y,side):
        self.X = X
        self.Y = Y
        self.side = side
        self.surface = pygame.Surface((self.side,self.side))
        self.surface.fill(colors['black'])
        self.color = set_color()
        self.visible = NO
        self.flower = set_flower()
    def get_position(self):
        x = self.X * self.side
        y = self.Y * self.side
        return (x,y)
    def get_surface(self):
        if self.visible:
            self.surface.fill(self.color)
        return self.surface
    def make_visible(self):
        self.visible = YES

class Terrain:
    terrain = []
    def __init__(self,width,height,side):
        for j in range(height/side):
            alist = []
            for i in range(width/side):
                alist.append( Tile(i,j,side) )
            self.terrain.append(alist)


if __name__ == '__main__':
    board = Terrain(105,49,24)
    for row in board.terrain:
        for tile in row:
            print tile.get_position(),
        print
        for tile in row:
            print str(tile.X) +','+ str(tile.Y),
        print

