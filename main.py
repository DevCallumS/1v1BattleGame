"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 20/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 2/06/2020|14:54

"""

import pygame
import os

pygame.init()

run = True

# WINDOW SETUP

WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1v1 Local Player")

# END OF WINDOW SETUP

class playerOne(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.x, self.y, self.width, self.height)


def redrawGameWindow():
    plrOne.draw(win)
    pygame.display.update()



plrOne = playerOne(0, 0, 64, 64)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    redrawGameWindow()



    

pygame.quit()