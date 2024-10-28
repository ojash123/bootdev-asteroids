from circleshape import CircleShape
from constants import *
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__timer = PLAYER_SHOOT_COOLDOWN
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 
    
    def draw(self, screen):
        pygame.draw.polygon(screen, color='white', points= self.triangle(), width= 2)
        return super().draw(screen)
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet = Shot(0, 0)
        bullet.position = self.triangle()[0]
        bullet.velocity = PLAYER_SHOOT_SPEED * direction

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.__timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.__timer < 0:
            self.shoot()
            self.__timer = PLAYER_SHOOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface= screen, color="WHITE", center= self.position, radius= self.radius, width= 2)

    def update(self, dt):
        self.position += self.velocity * dt