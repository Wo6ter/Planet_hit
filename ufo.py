import pygame
from constants import *
import math
from utils import rot_center
from file_loads import ufo_image


class Ufo:
    def __init__(self, screen):
        self.screen = screen
        self.image = ufo_image
        self.image = pygame.transform.scale(self.image, (UFO_WIDTH, UFO_HEIGHT))
        self.rect = self.image.get_rect()
        self.move_right = False
        self.move_left = False
        self.angle = -90

    def update(self):
        if self.move_right:
            self.angle += 1.5 # отвечает за скорость
        elif self.move_left:
            self.angle -= 1.5 # отвечает за скорость
        #                                                         ↓ отвечает за высоту
        self.rect.centerx = math.cos(math.radians(self.angle)) * UFO_RADIUS + WIDTH / 2
        self.rect.centery = math.sin(math.radians(self.angle)) * UFO_RADIUS + HEIGHT / 2
        self.screen.blit(rot_center(self.image, -self.angle-90), self.rect)