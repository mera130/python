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

class DiceGame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dice Roller")
        
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.SysFont('Arial', 32)
        
        # Load images
        self.bg = pygame.image.load("background(1).jpg").convert()
        pygame.image.load("dice1.png").convert_alpha(), 
        pygame.image.load("dice2.png").convert_alpha(), 
        pygame.image.load("dice3.png").convert_alpha(),  
        pygame.image.load("dice4.png").convert_alpha(),  
        pygame.image.load("dice5.png").convert_alpha(),  
        pygame.image.load("dice6.png").convert_alpha()  
        
        self.roll_button = Button(300, 400, 200, 100)
        self.current_dice = 1
        self.total_rolls = 0
        self.score = 0
        
    def roll_dice(self):
        self.current_dice = random.randint(1, 6)
        self.total_rolls += 1
        self.score += self.current_dice
        
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.roll_button_img, (300, 400))
        self.screen.blit(self.dice_images[self.current_dice - 1], (350, 200))
        
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        rolls_text = self.font.render(f"Rolls: {self.total_rolls}", True, self.WHITE)
        current_text = self.font.render(f"Current: {self.current_dice}", True, self.WHITE)
        
        self.screen.blit(score_text, (50, 50))
        self.screen.blit(rolls_text, (50, 100))
        self.screen.blit(current_text, (50, 150))
        
        pygame.display.update()
        
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.roll_button.clicked(pos):
                        self.roll_dice()
            
            self.draw()
            clock.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    game = DiceGame()
    game.run()