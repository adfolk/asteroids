import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


# Global variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_fired = pygame.sprite.Group()

    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (drawable, updatable, shots_fired)

    ship = Player(x, y, PLAYER_RADIUS)
    rock_pile = AsteroidField()

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(ship):
                print("Game over!")
                sys.exit(0)

            for shot in shots_fired:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()
            
        pygame.Surface.fill(screen, (0, 0, 0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()

