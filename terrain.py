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
           'lighter gray':(210,210,210),
           'mid brown':(141,92,43),
          }

blues = [(102,178,255),(0,128,255),(0,128,255),(0,0,255),(0,0,255),(0,0,153),]
flowers = {'daisy':colors['yellow'],'rose':colors['red'],
           'clover':colors['green']}
flower_pos = [(4,9),(10,4),(16,7)]

def set_color():
    #color = random.choice(colors.keys())
    #return colors[color]
    color = random.choice(blues)
    return color

def set_flower():
    if random.random() > 0.15:
        return (None,None)
    else:
        flower = random.choice(flowers.keys())
        quantity = random.choice([1,2,2,2,3,3])
        return (flowers[flower],quantity)

def draw_flower(surf,flower,num):
    new_surf = pygame.Surface(surf.get_size())
    for i in range(num):
        pygame.draw.circle(new_surf,flower,flower_pos[i], 3, 0)
    new_surf.set_colorkey((0,0,0))
    return new_surf


class Tile:
    def __init__(self,X,Y,side):
        self.X = X
        self.Y = Y
        self.side = side
        self.surface = pygame.Surface((self.side,self.side))
        self.surface.fill(colors['black'])
        self.color = set_color()
        self.visible = NO
        # for now flower_type is a color, later an image
        self.flower_type,self.flower_qty = set_flower()
    def get_position(self):
        x = self.X * self.side
        y = self.Y * self.side
        return (x,y)
    def get_surface(self):
        if self.visible:
            self.surface.fill(self.color)
            if self.flower_type:
                flwr = draw_flower(self.surface,self.flower_type,
                                   self.flower_qty)
                self.surface.blit(flwr,(0,0))
        return self.surface
    def make_visible(self):
        self.visible = YES
    def get_flower(self):
        if self.flower_qty > 0:
            self.flower_qty = self.flower_qty-1 
            return self.flower_type
        else:
            return None

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

