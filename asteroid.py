import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        course_angle = random.uniform(20, 50)
        split_vector1 = pygame.Vector2.rotate(self.velocity, course_angle)
        split_vector2 = pygame.Vector2.rotate(self.velocity, -course_angle)

        new_radii = self.radius - ASTEROID_MIN_RADIUS
        babby_x = self.position[0]
        babby_y = self.position[1]

        babby1 = Asteroid(babby_x, babby_y, new_radii)
        babby2 = Asteroid(babby_x, babby_y, new_radii)

        babby1.velocity = split_vector1 * 1.2
        babby2.velocity = split_vector2 * 1.2

