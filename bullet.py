import math
import pygame
from constants import *
from utils import checkcollisions
from file_loads import yellow_circle



class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ufo, target, planet):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = yellow_circle
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.angle = ufo.angle
        self.vertical = HEIGHT / 2 - ufo.rect.centery
        self.horizontal = WIDTH / 2 - ufo.rect.centerx
        self.rect.centerx = ufo.rect.centerx - math.cos(math.radians(self.angle)) * 40
        self.rect.centery = ufo.rect.centery - math.sin(math.radians(self.angle)) * 40

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.initialX = self.x
        self.initialY = self.y

        self.target = target
        self.planet = planet

    def update(self):
        self.y += self.vertical / 10 ** 4 * BULLET_SPEED
        self.x += self.horizontal / 10 ** 4 * BULLET_SPEED

        self.rect.y = self.y
        self.rect.x = self.x


        distanceX = self.initialX - self.x
        distanceY = self.initialY - self.y

        if (distanceX**2+distanceY**2)**0.5 > UFO_RADIUS-250/2 - 40:
            self.kill()
        if checkcollisions(self.x, self.y, 15, 15, self.target.rect.x, self.target.rect.y, 30, 30):
            self.kill()
            self.target.random_angle()
            self.planet.score += 1
            if self.planet.score % 10 == 0:
                self.planet.speed *= 1.5
                self.target.speed *= 1.5
            print(self.planet.score)



        self.screen.blit(self.image, (self.x, self.y))