import math
import pygame
import random
from constants import *
from file_loads import yellow_circle


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.image = yellow_circle
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        #self.angle = random.randint(0, 360)
        self.angle = 45
        self.speed = 0.5

    def random_angle(self):
        self.angle = random.randint(0, 360)

    def update(self):
        self.angle -= self.speed
        self.rect.centerx = math.cos(math.radians(self.angle)) * 131 + WIDTH / 2
        self.rect.centery = math.sin(math.radians(self.angle)) * 131 + HEIGHT / 2
        self.screen.blit(self.image, self.rect)