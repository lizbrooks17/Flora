#! /usr/bin/env python
## 10.April.15 Liz Brooks

# Classes for opening Instructions and Side panel

import pygame
from terrain import colors

def basket_positions(w,h,c,b):
    '''evenly distribute c number of items within the basket
    retun a list of upper left corner positions for each item'''
    ###width, height, count, buffer/padding
    if not c%2==0: c += 1
    r = min([ (h-3*b)/4, (w -(c/2+1)*b)/c ])
    pos = [None]*c
    for i in range(c/2):
        pos[i] = (i*b+2*i*r+b+r, b+r)
        pos[i+c/2] = (i*b+2*i*r+b+r, 2*b+3*r)
    return pos

class Basket:
    def __init__(self,width,height,capacity):
        self.surface = pygame.Surface((width,height))
        self.surface.fill(colors['mid brown'])
        self.content = [None]*capacity
        positions = basket_positions(width,height,capacity,12)
        for x in range(capacity):
            pygame.draw.circle(self.surface,colors['black'],
                               positions[x],12,2)
    def get_surface(self):
        return self.surface
    def add_flower(self,color):
        # find 1st open spot
        # if no open spots return False
        # draw a full circle on that spot
        # return True
        ## reblit the basket
    #def remove/gather/bunch flowers
        pass

class Sidepanel:
    def __init__(self,width,height,background):
        self.surface = pygame.Surface((width,height))
        self.surface.fill(background)

        if not pygame.font.get_init(): sys.exit("missing font module")
        text = pygame.font.SysFont('Arial',20)
        tcolor = colors['black']
        boxcolor = colors['lighter gray']
        inc = text.get_linesize()
        pad = 10   #padding

        # text strings
        tscore = text.render(u'Score',True,tcolor)
        tclock = text.render(u'Time Remaining',True,tcolor)
        tbasket = text.render(u'My Basket',True,tcolor)
        tgather = text.render(u'Gather',True,tcolor)

        scorebox = pygame.Surface((50,inc))
        scorebox.fill(boxcolor)
        scorepos = (2*pad+tscore.get_width(),pad)
        clockbox = pygame.Surface((80,inc))
        clockbox.fill(boxcolor)
        clockpos = (2*pad,3*pad+2*inc)
        basket = Basket(124,3*inc,8)

        self.surface.blit(tscore,(pad,pad))
        self.surface.blit(scorebox,scorepos)
        self.surface.blit(tclock,(pad,2*pad+inc))
        self.surface.blit(clockbox,clockpos)
        self.surface.blit(tbasket,(pad,4*pad+3*inc))
        self.surface.blit(basket.get_surface(),(2*pad,5*pad+4*inc))
        self.surface.blit(tgather,(pad,8*pad+7*inc))
    def get_surface(self):
        return self.surface


if __name__ == '__main__':
    basket = Basket(100,40,9)
