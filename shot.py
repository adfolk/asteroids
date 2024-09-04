import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.direction * PLAYER_SHOOT_SPEED * dt

