# 

import pygame
import random

class Hero(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('chgirl.png').convert_alpha()
        self.x = x
        self.y = y
        self.bullets = []
        self.frame = 0
        self.velocity = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.circle(screen, (255, 255, 255),
                               (bullet[0], bullet[1]), 6)

    def update(self, screen):
        # Update frame counter
        self.frame += 1

        remove = False
        # Move any existing bullets
        for bullet in self.bullets:
            bullet[0] += 1
            if bullet[0] > screen.get_width():
                remove = True

        # Delete any offscreen bullets
        if remove:
            del self.bullets[0]

        # Move hero
        self.y += self.velocity
        if self.y > screen.get_height() and self.velocity > 0:
            self.y = -self.image.get_height() + 70   # -101
        if self.y < -self.image.get_height() and self.velocity < 0:
            self.y = screen.get_height() - 70

    def shoot(self):
        if len(self.bullets) < 9:
            y_loc = self.y + 100
            self.bullets.append([170, y_loc])
            self.bullets.append([150, y_loc])
            self.bullets.append([130, y_loc])

    def move_down(self):
        self.velocity = 3

    def move_up(self):
        self.velocity = -3


class Villain(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('pkgirl.png').convert_alpha()
        self.x = x
        self.y = y
        self.bullets = []
        self.frame = 0
        self.velocity = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.circle(screen, (192, 192, 192),
                               (bullet[0], bullet[1]), 6)

    def update(self, screen):
        if random.randint(1, 60) == 1:
            self.shoot()
        if random.randint(1, 100) == 1:
            self.velocity *= -1

        # Update frame counter
        self.frame += 1

        remove = False
        # Move any existing bullets
        for bullet in self.bullets:
            bullet[0] -= 1
            if bullet[0] < 0:
                remove = True

        # Delete any offscreen bullets
        if remove:
            del self.bullets[0]

        # Move hero
        self.y += self.velocity
        if self.y > screen.get_height() and self.velocity > 0:
            self.y = -self.image.get_height() + 70   # -101
        if self.y < -self.image.get_height() and self.velocity < 0:
            self.y = screen.get_height() - 70

    def shoot(self):
        if len(self.bullets) < 15:
            y_loc = self.y + 100
            self.bullets.append([self.x - 110, y_loc])
            self.bullets.append([self.x - 90, y_loc])
            self.bullets.append([self.x - 70, y_loc])

    def move_down(self):
        self.velocity = 3

    def move_up(self):
        self.velocity = -3

def init():
    width, height = 800, 600
    pygame.init()
    # Screen
    return pygame.display.set_mode((width, height))


def main(screen):
    clock = pygame.time.Clock()
    hero = Hero(60, 100)
    villain = Villain(640, 400)
    villain.move_up()
    running = True
    while running:
        screen.fill((0, 0, 0))          # Redraw background
        hero.draw(screen)
        villain.draw(screen)
        pygame.display.flip()           # Display screen in window
        hero.update(screen)
        villain.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.shoot()
                if event.key == pygame.K_s:
                    hero.move_down()
                if event.key == pygame.K_w:
                    hero.move_up()
        clock.tick(40)

screen = init()
main(screen)