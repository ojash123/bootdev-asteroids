import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    afield = AsteroidField()
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='#000000')
        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for ast in asteroids:
            if(ast.collided(p)):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if ast.collided(bullet):
                    ast.split()
                    bullet.kill()
        pygame.display.flip()
        dt = clk.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()