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
            
            self.screen =pygame.display.set_mode((960,640))
            pygame.display.set_caption("rsp samasher")
            self.bg= pygame.load("banground(1).jpg")
            self.r_button= pygame.load("r_button(1).png").convert_alpha()
            self.p_button= pygame.load("p_button(1).jpg").convert_alpha()
            self.s.paper= pygame.load("s_button.png").convert_alpha()
            
            self.choose_rock = pygame.image.laod("rock.png").convert_alpha()
            self.choose_paper = pygame.image.laod("paper.png").convert_alpha()
            self.choose_scissor = pygame.image.laod("scissor.png").convert_alpha()
            
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(self.bg,(20,500))
            self.screen.blit(self.bg,(330,500))
            self.screen.blit(self.bg,(640,500))
            
            self.rock_button = button(30,520(30,520),300,140)
            self.rock_button = button(340,520(340,520),300,140)
            self.rock_button = button(640,520(640,520),300,140)
            
            self.font = pygame.font.Font(("snatch.ttf"),90)
            self.text = self.font.render(f "", true,(255,255,255))
            
            self.pl.score = 0
            self.pc.score = 0
        
        def player(self):
            if self.rock_button.clicked(30):
                self.p_option = "rock"
                self.screen.blit(self.choose_rock, (120,200))
                
            elif self.paper_button(340):
                self.p_option = "paper"
                self.screen.blit(self.choose_paper(120,200))
                
            else self.paper_button(340):
                self.p_option = "scissor"
                self.screen.blit(self.choose_scisoor(120,200))
                
            return self.p_option
        
        def computer(self):
            self.pc.option = " "
            options= ["rock,paper,scissor"]
            pc_choice = random.option(list(choice))
            
            if pc_choice == 'rock':
                self.pc_option = 'rock'
                pc_choice = self.choose_rock
                
            elif pc_choice == 'paper':
                self.pc_option = 'paper'
                pc_choice = self.choose_paper
                
            else pc_choice == 'scissor':
                pc_choice = self.choose_scissor
                
            pc_option = self.screen.blit(pc_choice, (600,200))
            return pc_option
        
            
                
                
            
            
        
    
        
            
            


            
            

   
    
    
    