import pygame
from settings import *

class Score:
    def __init__(self, x, y):
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font(None, 30)
        self.surf = self.font.render(str(self.score), True, 'White')
        self.rect = self.surf.get_rect(center=(x, y))
        self.high_score_surf = self.font.render("High Score: " + str(self.high_score), True, 'White')
        self.high_score_rect = self.high_score_surf.get_rect(center=(x, y - 25))

    def updateHighScore(self):
        ''' Update the high score if self.score is greater than self.high_score '''
        if int(self.score) > int(self.high_score):
            self.high_score = int(self.score)

    def update(self):
        ''' Update the score based on the self.score value. '''
        self.updateHighScore()
        self.surf = self.font.render(str(self.score), True, 'White')
        self.high_score_surf = self.font.render("High Score: " + str(self.high_score), True, 'White')  
