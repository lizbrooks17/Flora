#! /usr/bin/env python
## 19.March.15 Liz Brooks

# Classes for Tiles and game Board

import pygame
import random

all_land = { 'black':(0,0,0),
             'red':(255,0,0),
             'blue':(0,0,255),
             'green':(0,255,0),
             'white':(255,255,255), }

blues = [(102,178,255),(0,128,255),(0,128,255),(0,0,255),(0,0,255),(0,0,153),]

def set_color():
    #color = random.choice(all_land.keys())
    #return all_land[color]
    color = random.choice(blues)
    return color

def set_flower():
    return None

class Tile:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        self.surface = pygame.Surface((20,20))
        #self.color = set_color()
        self.surface.fill(set_color())
        self.flower = set_flower()
    def get_position(self):
        return (self.X,self.Y)
    def get_surface(self):
        #self.surface.fill(self.color)
        return self.surface

class Terrain:
    terrain = []
    def __init__(self,X,Y):
        for j in range(Y/20):
            alist = []
            for i in range(X/20):
                alist.append( Tile(i*20,j*20) )
            self.terrain.append(alist)


if __name__ == '__main__':
    board = Terrain(105,49)
    for row in board.terrain:
        for tile in row:
            print tile.get_position(),
        print


