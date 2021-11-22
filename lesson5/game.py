from abc import abstractmethod
from abc import ABC
import math as m
import pygame
from pygame.draw import *
from random import randint
import sys

pygame.init()
pygame.font.init()
FPS = 20
border = (800, 600)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
start_menu = pygame.font.SysFont('Comic Sans Ms', 40)


class Target(ABC):  # Абстрактный класс мишени
    def __init__(self):
        self.x = randint(10, 790)
        self.y = randint(10, 590)
        self.r = randint(10, 20)
        self.v_x = randint(3, 5)
        self.v_y = randint(3, 5)
        self.color = COLORS[randint(0, 5)]

    @abstractmethod
    def draw(self, surface):
        pass

    def move(self):
        self.x += self.v_x
        self.y -= self.v_y
        #self.color = COLORS[randint(0, 5)]


    def collision(self):
        if (self.x + self.r >= 800) or (self.x - self.r <= 0):
            self.v_x = -1 * self.v_x
        if (self.y + self.r >= 600) or (self.y - self.r <= 0):
            self.v_y = -1 * self.v_y


class Ball(Target):    # рисует шары

    def draw(self, surface):
        circle(surface,
               self.color,
               (self.x, self.y),
               self.r)


class Triangle(Target): # рисует "правильные" треугольники

    def draw(self, surface):
        rect(surface,
             self.color,
             (self.x, self.y, self.r, self.r)
             )




surface = pygame.display.set_mode(border)





pygame.display.update()
clock = pygame.time.Clock()
finished = False
surface.fill((255, 255, 255))
score = 0
level = True
pool = [Ball() for i in range(10)]
pool1 = [Triangle() for i in range(10)]
f1 = pygame.font.SysFont('Comic Sans MS', 40)
Start_Screen = True
surface.fill(BLACK)
while not finished:
    clock.tick(FPS)
    Score1 = 'Score: ' + str(score)  # отоброжение очков на экране
    score_info = f1.render(Score1, True, (0, 255, 255))
    surface.blit(score_info, (0, 0))
    if Start_Screen:
        hello_message = start_menu.render('Выберете уровень сложности', True, WHITE)
        normal = start_menu.render('1 - нормально', True, WHITE)
        hard = start_menu.render('2 - сложно', True, WHITE)
        surface.blit(hello_message, (100, 200))
        surface.blit(normal, (100, 300))
        surface.blit(hard, (100, 400))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            Start_Screen = False
        if event.type == pygame.KEYDOWN:
            Start_Screen = False
            level = False
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in pool:
                if (abs(event.pos[0] - i.x) < i.r) and (abs(event.pos[1] - i.y) < i.r):
                    score += 1



    if Start_Screen == False:
        for j in pool:
            j.draw(surface)
            j.move()
            j.collision()
        pygame.display.update()

        for i in pool1:
            i.draw(surface)
            i.move()
            i.collision()
        pygame.display.update()
        Score1 = 'Score: ' + str(score)  # отоброжение очков на экране
        score_info = f1.render(Score1, True, (0, 255, 255))
        surface.blit(score_info, (0, 0))
        if level == False:
             surface.fill(COLORS[randint(0, 5)])
        else:
            surface.fill(BLACK)




pygame.quit()
