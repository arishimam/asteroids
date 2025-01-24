import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collision(p1):
                print("Game over")
                return 

            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split()
            
        screen.fill("black")

        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
