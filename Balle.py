import random

import pygame
import core

hauteur = 800
largeur = 800
balls = []

def setup():
    print("setup")
    global balls
    core.WINDOW_SIZE = [hauteur, largeur]
    core.fps=30

    for i in range(0,15) :
        x = random.randint(0, largeur)
        y = random.randint(0, hauteur)

        xd = random.uniform(-5, 5)
        yd = random.uniform(-5, 5)
        r  = random.randint(10,50)
        balls = balls + [[x, y, xd, yd, r]]


def run():
    print("Run")

    for b in balls :
        print(b)
        pygame.draw.circle(core.screen, (50,210,220), (b[0],b[1]), b[4])

    for b in balls :
        b[0] = b[0] + b[2]
        b[1] = b[1] + b[3]

    for b in balls :
        if b[0] < b[4] or b[0] > largeur - b[4]:
            b[2] = -b[2]
        if b[1] < b[4] or b[1] > hauteur - b[4]:
            b[3] = -b[3]





core.main(setup, run)