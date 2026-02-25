import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (shots, updatable, drawable)
    asteroidfields = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for aster in asteroids:
            if player.collides_with(aster):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(aster):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()

        screen.fill("black")
        for drawings in drawable:
            drawings.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
