import random
import pygame

class button():
    
    def __init__(self,x,y,pos,width,height):
         self.x = x
         self.y = y
         self.pos = pos
         self.width = width
         self.height = height
         
    def clicked(self,pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos [0] > self.x and self.pos[0]<self.x + self.width:
            if self.pos[1]>self.y and self.pos [1] < self.y +self.height:
                return True
        return False
    
    class rspgame():
        def __init__(self):
            pygame.init()
            
            self.screen = pygame.display.set_mode((960,640))
            pygame.display.set_caption("rsp samasher")

   
    
    
    