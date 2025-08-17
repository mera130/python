import random
import pygame

class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
         
    def clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    
class RSPGame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RSP Samasher")
        
        self.bg = pygame.image.load("background(1).jpg").convert()
        self.r_button = pygame.image.load("r_button(1).png").convert_alpha()
        self.p_button = pygame.image.load("p_button(1).jpg").convert_alpha()
        self.s_button = pygame.image.load("s_button.png").convert_alpha()  
        
        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissor = pygame.image.load("scissor.png").convert_alpha()
        
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_button, (20, 500))
        self.screen.blit(self.p_button, (330, 500))
        self.screen.blit(self.s_button, (640, 500))
        
        
        self.rock_button = Button(30, 520, 300, 140)
        self.paper_button = Button(340, 520, 300, 140)
        self.scissors_button = Button(640, 520, 300, 140)
        
        
        self.font = pygame.font.Font("snatch.ttf", 90)
        self.text = self.font.render("", True, (255, 255, 255))
    
        self.player_score = 0
        self.computer_score = 0
    
    def player(self):
        pos = pygame.mouse.get_pos()  
        if self.rock_button.clicked(pos):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_button.clicked(pos):  
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))  
        elif self.scissors_button.clicked(pos):  
            self.p_option = "scissor"
            self.screen.blit(self.choose_scissor, (120, 200))
        return self.p_option
    
    def computer(self):
        options = ["rock", "paper", "scissor"] 
        pc_choice = random.choice(options)  
        
        if pc_choice == "rock":
            self.screen.blit(self.choose_rock, (600, 200))
        elif pc_choice == "paper":
            self.screen.blit(self.choose_paper, (600, 200))
        else:
            self.screen.blit(self.choose_scissor, (600, 200))
        return pc_choice