from locale import normalize
import pygame
from random import choice
from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self.surf.fill('white')

        self.speed = 3
        self.direction = pygame.math.Vector2(choice([-1, 1]), choice([-1, 1]))

    def reset(self):
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self.direction = pygame.math.Vector2(choice([-1, 1]), choice([-1, 1]))

    def collisions(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction.y *= -1
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.direction.y *= -1

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction.normalize() * self.speed
        
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        
        self.collisions()

    def update(self):
        self.move()
