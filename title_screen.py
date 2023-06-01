import pygame
import math
import time

from constants import *
from utils import checkcollisions


def title_screen(screen, bg, button, title_text, start):
    title_screen = True
    while title_screen:
        clicked = False
        space = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space = True


        mousex, mousey = pygame.mouse.get_pos()

        if clicked and checkcollisions(mousex, mousey, 3, 3, WIDTH/2 - button.get_width()/2, 396, button.get_width(), button.get_height()) or space:
            title_screen = False

        screen.fill(WHITE)
        screen.blit(bg, (0,0))
        screen.blit(title_text, (WIDTH/2 - title_text.get_width()/2, HEIGHT/2 - 83.5 + math.sin(time.time()*5)*5 - 25))
        screen.blit(button, (WIDTH/2 - button.get_width()/2, 396))
        screen.blit(start, (WIDTH/2 - start.get_width()/2, 400))
        pygame.display.update()