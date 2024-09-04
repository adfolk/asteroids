import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)
        self.position = pygame.Vector2(self.x, self.y)
        self.rotation = 0
        self.shot_timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        point_list = self.triangle()
        white_line = (255, 255, 255)
        pygame.draw.polygon(screen, white_line, point_list, width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        print(self.shot_timer)
        if self.shot_timer > 0:
            return
        else:
            self.shot_timer += PLAYER_SHOOT_COOLDOWN
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            newx = self.position[0]
            newy = self.position[1]
            newshot = Shot(newx, newy, SHOT_RADIUS, forward)

    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            dt = 0 - dt
            self.rotate(dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

