import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((15, 85))
        self.rect = self.surf.get_rect(center=(WIDTH // 10, HEIGHT // 2))
        self.surf.fill('white')

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def checkCollisions(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def move(self):
        self.rect.y += (self.direction.x * self.speed) + (self.direction.y * self.speed)
        self.checkCollisions()

    def update(self):
        self.move()

    

    