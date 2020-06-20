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
clock = pygame.time.Clock()

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
        self.velocity = 5
        self.left = False
        self.right = False


    def draw(self, win):
        # if self.left:
            
        # else: 
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))


def redrawGameWindow():
    plrOne.draw(win)
    win.fill((0,0,0))
    pygame.display.update()



plrOne = playerOne(0, 0, 64, 64)

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and plrOne.x > plrOne.velocity:
        plrOne.x -= plrOne.velocity
        plrOne.left = True
        plrOne.right = False
    elif keys[pygame.K_d] and plrOne.x < WIDTH - plrOne.width - plrOne.velocity:
        plrOne.x += plrOne.velocity
        plrOne.left = False
        plrOne.right = True

        



    redrawGameWindow()



    

pygame.quit()