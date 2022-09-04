import pygame, sys, os
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        
        if not os.path.exists('highScore.txt'):
            with open('./highScore.txt', 'w') as f:
                f.write('0, 0')
                
        self.clock = pygame.time.Clock()
        self.level = Level()

    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.updateHighScores()
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')
            
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
