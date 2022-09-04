import pygame
from settings import *
from player import Player
from enemy import Enemy
from ball import Ball
from score import Score

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.player = Player()
        self.enemy = Enemy()
        self.ball = Ball()
        self.player_score = Score(WIDTH // 3, HEIGHT // 10)
        self.enemy_score = Score(WIDTH * 2 // 3, HEIGHT // 10)
        self.loadHighScores()

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.player.direction.x = -1
        else:
            self.player.direction.x = 0

        if keys[pygame.K_s]:
            self.player.direction.y = 1
        else:
            self.player.direction.y = 0

        if keys[pygame.K_UP]:
            self.enemy.direction.x = -1
        else:
            self.enemy.direction.x = 0

        if keys[pygame.K_DOWN]:
            self.enemy.direction.y = 1
        else:
            self.enemy.direction.y = 0

    def collisions(self):
        self.checkBallWallCollisions()
        self.checkPaddleBallCollisions()

    def checkBallWallCollisions(self):
        if self.ball.rect.left < 0:
            self.enemy_score.score += 1
            self.enemy_score.update()
            self.ball.reset()
        elif self.ball.rect.right > WIDTH:
            self.player_score.score += 1
            self.player_score.update()
            self.ball.reset()

    def checkPaddleBallCollisions(self):
        if self.player.rect.colliderect(self.ball.rect) and self.ball.rect.left > self.player.rect.centerx:
            self.ball.rect.left = self.player.rect.right
            self.ball.direction.x *= -1
        if self.enemy.rect.colliderect(self.ball.rect) and self.ball.rect.right < self.enemy.rect.centerx:
            self.ball.rect.right = self.enemy.rect.left
            self.ball.direction.x *= -1

    def loadHighScores(self):
        with open('./highScore.txt', 'r') as f:
            scores = f.read().split(", ")
            self.player_score.high_score = int(scores[0])
            self.enemy_score.high_score = int(scores[1])
            self.player_score.update()
            self.enemy_score.update()

    def updateHighScores(self):
        with open('./highScore.txt', 'w') as f:
            f.write(f"{int(self.player_score.high_score)}, {int(self.enemy_score.high_score)}")

    def update(self):
        self.player.update()
        self.enemy.update()
        self.ball.update()

    def display(self):
        self.screen.blit(self.player.surf, self.player.rect)
        self.screen.blit(self.enemy.surf, self.enemy.rect)
        self.screen.blit(self.ball.surf, self.ball.rect)
        self.screen.blit(self.player_score.surf, self.player_score.rect)
        self.screen.blit(self.enemy_score.surf, self.enemy_score.rect)
        self.screen.blit(self.player_score.high_score_surf, self.player_score.high_score_rect)
        self.screen.blit(self.enemy_score.high_score_surf, self.enemy_score.high_score_rect)

    def run(self):
        self.input()
        self.update()
        self.collisions()
        self.display()
