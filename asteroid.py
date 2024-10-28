from circleshape import CircleShape
from constants import *
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface= screen, color="WHITE", center= self.position, radius= self.radius, width= 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        r1 = self.velocity.rotate(angle)
        r2 = self.velocity.rotate( -angle)
        rad1 = self.radius - ASTEROID_MIN_RADIUS
        mini1 = Asteroid(self.position.x, self.position.y, rad1)
        mini1.velocity = r1 * 1.2
        mini2 = Asteroid(self.position.x, self.position.y, rad1)
        mini2.velocity = r2 * 1.2
        

    