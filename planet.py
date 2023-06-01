import random
from constants import *
from utils import rot_center
from file_loads import *


class Planet:


    def __init__(self, screen, target):
        self.screen = screen
        self.planet_image = planet_image
        self.planet_image = pygame.transform.scale(self.planet_image, (250, 250))
        self.score_image = button_image
        self.angle = -90
        self.rect = self.planet_image.get_rect()
        self.score = 0
        self.score_text = ""
        self.speed = 0.5

        self.target = target

    def check_score(self):
        if self.score == 10:
            self.speed += 0.2

    def update(self):
        if random.randint(0,10000-self.score*10) == 69:
            self.speed = -self.speed
            self.target.speed = -self.target.speed
        self.score_text = font_32.render(str(self.score), True, WHITE)
        self.angle += self.speed # gets higher, when score gets higher
        self.screen.blit(rot_center(self.planet_image, self.angle - 90), (WIDTH / 2 - 125, HEIGHT / 2 - 125))
        self.screen.blit(self.score_image, (WIDTH / 2 - self.score_image.get_width() / 2, 600))
        self.screen.blit(self.score_text, (WIDTH / 2 - 10, 605))