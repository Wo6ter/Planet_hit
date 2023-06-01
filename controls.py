import pygame
import time
from bullet import Bullet


def events(screen, ufo, bullets, target, planet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            print(f"time is {time.time()}")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ufo.move_right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ufo.move_left = True
            elif event.key == pygame.K_SPACE and time.time() > last_shot + 0.5:
                new_bullet = Bullet(screen, ufo, target, planet)
                bullets.add(new_bullet)
                last_shot = time.time()
                print(f"last is {last_shot}")
                print(f"last +5 {last_shot + 5}")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet(screen, ufo, target, planet)
            bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ufo.move_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ufo.move_left = False