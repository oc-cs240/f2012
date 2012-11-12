# 

import pygame

class Hero(object):
    def __init__(self):
        self.image = pygame.image.load('chgirl.png').convert_alpha()
        self.x = 60
        self.y = 100
        self.bullets = [[130, 200], [150, 200], [170, 200]]
        self.frame = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.circle(screen, (255, 255, 255),
                               (bullet[0], bullet[1]), 6)

    def update(self, screen):
        # Update frame counter
        self.frame += 1

        # Move any existing bullets
        for bullet in self.bullets:
            bullet[0] += 1

        # Move hero
        self.y += 1
        if self.y > screen.get_height():
            print len(self.bullets)
            self.y = 0
        # Throw 3 more snowballs every 20 pixels of movement
        if self.y % 100 == 0:
            self.bullets.append([130, self.y + 100])
            self.bullets.append([150, self.y + 100])
            self.bullets.append([170, self.y + 100])


def init():
    width, height = 800, 600
    pygame.init()
    # Screen
    return pygame.display.set_mode((width, height))


def main(screen):
    clock = pygame.time.Clock()
    hero = Hero()
    running = True
    while running:
        screen.fill((0, 0, 0))          # Redraw background
        hero.draw(screen)
        pygame.display.flip()           # Display screen in window
        hero.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False
        clock.tick(40)

screen = init()
main(screen)