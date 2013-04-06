# A basic pygame template

import pygame

WINDOW_TITLE = 'PyGame'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def init():
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def main(screen):
    running = True
    while running:
        screen.fill((0, 0, 0))          # Redraw background
        pygame.display.flip()           # Display screen in window

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False


screen = init()
main(screen)