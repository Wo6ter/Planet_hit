import pygame
from pygame.sprite import Group

import controls
from constants import *
from ufo import Ufo
from title_screen import title_screen
from planet import Planet
from target import Target
from file_loads import font_32, font_70, bg_image, button_image


def main():
    pygame.init()

    # if bg -> title_text = font_70.render("Planet hit", True, (0, 255, 255))
    title_text = font_70.render("Planet hit", True, (128, 128, 128))
    start_text = font_32.render("START", True, WHITE)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planet hit")

    button = button_image
    bg = bg_image
    bg = pygame.transform.scale(bg, (1500, HEIGHT))

    bullets = Group()
    target = Target(screen)
    ufo = Ufo(screen)
    planet = Planet(screen, target)
    title_screen(screen, bg, button, title_text, start_text)

    while True:

        clock = pygame.time.Clock()
        clock.tick(FPS)
        screen.blit(bg, (0, 0))
        controls.events(screen, ufo, bullets, target, planet)

        ufo.update()
        planet.update()
        target.update()
        bullets.update()


        pygame.display.update()


if __name__ == "__main__":
    main()
