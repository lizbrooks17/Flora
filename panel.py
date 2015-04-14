#! /usr/bin/env python
## 10.April.15 Liz Brooks

# Classes for opening Instructions and Side panel

import pygame
from terrain import colors, flowers

class Score:
    def __init__(self,size,location,offset,background):
        self.surface = pygame.Surface(size)
        self.position = location
        self.offset = offset
        self.color = background
        self.surface.fill(self.color)
        self.score = 0
    def get_surface(self):
        return self.surface
    def get_position(self):
        x = self.position[0] + self.offset
        y = self.position[1]
        return (x,y)
    def update_score(self,num):
        text = pygame.font.SysFont('Arial',20)
        self.score += num
        tnum = text.render(str(self.score),True,colors['black'])
        self.surface.fill(self.color)
        self.surface.blit(tnum,(10,0))
        return self.surface

class Clock:
    def __init__(self,size,location,offset,background):
        self.surface = pygame.Surface(size)
        self.position = location
        self.offset = offset
        self.color = background
        self.surface.fill(self.color)
    def get_surface(self):
        return self.surface
    def get_position(self):
        x = self.position[0] + self.offset
        y = self.position[1]
        return (x,y)
    def update_time(self,time):
        text = pygame.font.SysFont('Arial',20)
        ttime = text.render(str(time),True,colors['black'])
        self.surface.fill(self.color)
        self.surface.blit(ttime,(20,0))
        return self.surface

def basket_positions(w,h,c,b):
    '''evenly distribute c number of items within the basket
    retun a list of upper left corner positions for each item'''
    ###width, height, count, buffer/padding?
    if not c%2==0: c += 1
    r = min([ (h-3*b)/4, (w -(c/2+1)*b)/c ])
    pos = [None]*c
    for i in range(c/2):
        pos[i] = (i*b+2*i*r+b+r, b+r)
        pos[i+c/2] = (i*b+2*i*r+b+r, 2*b+3*r)
    return pos

class Basket:
    def __init__(self,width,height,capacity,location,offset):
        self.surface = pygame.Surface((width,height))
        self.surface.fill(colors['mid brown'])
        self.contents = [None]*capacity
        self.positions = basket_positions(width,height,capacity,12)
        for x in range(capacity):
            pygame.draw.circle(self.surface,colors['black'],
                               self.positions[x],12,2)
        self.position = location
        self.offset = offset
    def get_surface(self):
        return self.surface
    def get_position(self):
        x = self.position[0] + self.offset
        y = self.position[1]
        return (x,y)
    def add_flower(self,color):
        # if no open spots return False
        if not None in self.contents:
            return False
        else:
            # find 1st open spot
            i = self.contents.index(None)
            self.contents[i] = color
            # draw a full circle on that spot
            pygame.draw.circle(self.surface,color,self.positions[i],12,0)
            return True
    def remove_flower(self,color):
        if color in self.contents:
            i = self.contents.index(color)
            self.contents[i] = None
            pygame.draw.circle(self.surface,colors['mid brown'],
                               self.positions[i],12,0)
            pygame.draw.circle(self.surface,colors['black'],
                               self.positions[i],12,2)
    def check_bq(self,colors):
        check = True
        for color in colors:
            if not color in self.contents:
                check = False
        return check

class Bouquet:
    def __init__(self,size,location):
        self.surface = pygame.Surface(size)
        self.surface.fill(colors['mid brown'])
        self.flowers = flowers.values() #color triplet for now
        for i in range(3):
            pygame.draw.circle(self.surface,self.flowers[i],(i*8+8,12),8,0)
        self.position = pygame.Rect(location,size)
    def get_surface(self):
        return self.surface


class Sidepanel:
    def __init__(self,width,height,offset,background):
        self.surface = pygame.Surface((width,height))
        self.surface.fill(background)
        self.offset = offset

        if not pygame.font.get_init(): sys.exit("missing font module")
        text = pygame.font.SysFont('Arial',20)
        tcolor = colors['black']
        boxcolor = colors['lighter gray']
        inc = text.get_linesize()
        pad = 10   #padding

        # text strings & contents
        tscore = text.render(u'Score',True,tcolor)
        tclock = text.render(u'Time Remaining',True,tcolor)
        tbasket = text.render(u'My Basket',True,tcolor)
        #tgather = text.render(u'Gather',True,tcolor)
        self.scorebox = Score((width-(4*pad+tscore.get_width()),inc),
                              (2*pad+tscore.get_width(),pad),offset,boxcolor)
        self.clockbox = Clock((tclock.get_width()-2*pad,inc),
                              (2*pad,3*pad+2*inc),offset,boxcolor)
        self.basket = Basket(124,3*inc,8,(2*pad,5*pad+4*inc),offset)
        self.bouquet1 = Bouquet((50,2*inc),(2*pad,8*pad+7*inc))
        self.bouquet2 = Bouquet((50,2*inc),(.5*width+pad,8*pad+7*inc))

        self.surface.blit(tscore,(pad,pad))
        self.surface.blit(self.scorebox.get_surface(),self.scorebox.position)
        self.surface.blit(tclock,(pad,2*pad+inc))
        self.surface.blit(self.clockbox.get_surface(),self.clockbox.position)
        self.surface.blit(tbasket,(pad,4*pad+3*inc))
        self.surface.blit(self.basket.get_surface(),self.basket.position)
        self.surface.blit(self.bouquet1.get_surface(),self.bouquet1.position)
        self.surface.blit(self.bouquet2.get_surface(),self.bouquet2.position)
    def get_surface(self):
        return self.surface
    def get_position(self):
        return (self.offset,0)
    def get_buttons(self):
        return [self.bouquet1,self.bouquet2]
    def gather(self,bouquet):
        flowers = bouquet.flowers
        if self.basket.check_bq(flowers):
            for flower in flowers:
                self.basket.remove_flower(flower)
            return True
        else:
            print "not enough flowers"
            return False


if __name__ == '__main__':
    basket = Basket(100,40,9,(0,0))
